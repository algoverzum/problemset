# Deployment overview

A new problem (or a change to an existing problem) needs to be added to three services:
- the "planets" database in Firestore, which contains all the problem statements and metadata.
- the "testcases/planets" directory in the Firebase Storage bucket, which is used by the IDE to display test cases to users.
- the judge server, which stores the test cases that the submissions are run against.

## Manual deployment

A manual deployment involves the following steps:
1. Generate the test cases with `task-maker-rust`
2. Upload the problem statements with the `tools/importProblems.ts` script from the Planets repository
3. Upload the test cases to Firebase Storage with the `tools/uploadTestcases.ts` script from the Planets repository
4. Pull the changes to the git repository on the judge server and run `task-maker-rust` there

The two scripts require a **service account key** for the Firebase project whose path is provided in the `FIREBASE_CRED_PATH` environment variable and the name of the storage bucket (`STORAGE_BUCKET`). Additionally, SSH access to the judge server is required.

## Automated deployment

`tools/auto_deploy.sh` is a script that automates the deployment process. It is designed to run on the judge server, where it fetches the latest changes, generates the test cases and uploads all the necessary data to Firebase. The script can either be run by a cron job or triggered whenever a new commit is pushed to the repository using a [Webhook](https://docs.github.com/en/webhooks) (this is what we use in production).

### Setup (on the Judge server)

Install a recent version of Node.js and npm:

```bash
curl -sL https://deb.nodesource.com/setup_25.x | sudo bash -
sudo apt install -y nodejs
```

Clone the `planets` repository. The script assumes that it is located beside `planets-problemset`. Then, fetch the dependencies for the scripts:
```bash
cd planets/tools
npm install
npm run build
```

Generate a service account key for Firebase and transfer it to the server. Its path can be specified via `ALGOPRO_CREDENTIAL_PATH`/`MATFIZ_CREDENTIAL_PATH`.

Now, the script can be run manually to test whether it works. (FIXME: due to some weirdness with `task-maker-rust`, the script needs to be run as root).

If everything works okay, we can move on to setting up the webhook. This uses the [adnanh/webhook](https://github.com/adnanh/webhook) service to trigger the deployment script. Install it from the Ubuntu repositories:

```bash
sudo apt-get install webhook
```

Then, create the configuration file (`/etc/webhook.yaml `) with the following content:

```
- id: push
  execute-command: /path/to/planets-problemset/tools/auto_deploy.sh
  response-message: ok
  command-working-directory: /path/to/planets-problemset
  trigger-rule:
      match:
        type: payload-hmac-sha256
        secret: <your secret>
        parameter:
          source: header
          name: X-Hub-Signature-256

```
`<your secret>` is a pre-shared secret between GitHub and the server that will be used to verify the authenticity of the webhook requests. You can generate a random secret with `openssl rand -base64 32`.

Then, create a systemd service to run the webhook server and set its content to be the following:

```bash
sudo systemctl edit webhook
```

```ini
[Unit]
ConditionPathExists=
ConditionPathExists=/etc/webhook.yaml

[Service]
ExecStart=
ExecStart=/usr/bin/webhook -nopanic -hooks /etc/webhook.yaml -ip 127.0.0.1 -port 9899 -urlprefix webhook
User=root
Group=root
```

(As the webhooks, and thus the deployment script runs as root right now, the service account keys should be in `/root`).

Lastly, enable and start the service:

```bash
sudo systemctl enable webhook
sudo systemctl start webhook
```


As GitHub requires webhooks to be served over HTTPS, we need to set up a reverse proxy with Nginx and HTTPS with Let's Encrypt. For this, install the dependencies:

```bash
sudo apt install -y nginx certbot python3-certbot-nginx
```

Add the following lines to the `server {}` block in the Nginx configuration (e.g. `/etc/nginx/sites-available/default`) to proxy requests to the webhook service:

```
    location ~ ^/webhook/ {
       proxy_pass http://webhooks;
    }
```

Then, add the following lines to the end of the file to define the `webhooks` upstream:

```
upstream webhooks {
    server 127.0.0.1:9899 fail_timeout=5;
}
```

Finally, obtain an SSL certificate for the server and reload Nginx:

```bash
sudo certbot --nginx -d your-domain.com
sudo systemctl reload nginx
```

The last step is to add the webhook in the GitHub repository settings. See the [GitHub documentation](https://docs.github.com/en/webhooks) for more details. The payload URL should be `https://your-domain.com/webhook/push` and the content type should be `application/json`. The secret should be the same as the one specified in the webhook configuration file on the server.
