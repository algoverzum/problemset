#!/usr/bin/env bash

REPO_PATH=${1:-$(git rev-parse --show-toplevel)}
PLANETS_TOOLS_PATH=${PLANETS_TOOLS_PATH:-"$REPO_PATH/../planets/tools/dist"}
ALGOPRO_CREDENTIAL_PATH=${ALGOPRO_CREDENTIAL_PATH:-"$HOME/algopro-service-account.json"}
MATFIZ_CREDENTIAL_PATH=${MATFIZ_CREDENTIAL_PATH:-"$HOME/matfiz-service-account.json"}

if [ ! -d "$REPO_PATH" ]; then
    echo "ERROR: The specified repository path '$REPO_PATH' does not exist."
    exit 1
fi

cd "$REPO_PATH" || exit 1

if ! git status >/dev/null; then
    echo "ERROR: The specified path '$REPO_PATH' is not a git repository."
    exit 1
fi

LOCK_FILE="$REPO_PATH/.auto_deploy.lock"
if ( set -o noclobber; echo "$$" > "$LOCK_FILE" ) 2>/dev/null; then
    trap 'rm -f "$LOCK_FILE"' EXIT INT TERM
else
    if [ -r "$LOCK_FILE" ]; then
        LOCK_PID=$(cat "$LOCK_FILE")
        if [ -n "$LOCK_PID" ] && kill -0 "$LOCK_PID" 2>/dev/null; then
            echo "ERROR: Another deployment is already running (PID $LOCK_PID)."
            exit 1
        fi
    fi
    echo "Stale lock detected, taking over."
    echo "$$" > "$LOCK_FILE"
    trap 'rm -f "$LOCK_FILE"' EXIT INT TERM
fi

echo "Checking for updates to repository at '$REPO_PATH'..."

OLD_COMMIT=$(git rev-parse HEAD)

if ! git pull >/dev/null; then
    echo "ERROR: Failed to pull updates from remote repository."
    exit 1
fi

NEW_COMMIT=$(git rev-parse HEAD)

if [ "$OLD_COMMIT" == "$NEW_COMMIT" ]; then
    echo "No updates were found. Exiting."
    exit 0
fi

echo "Updated from commit $OLD_COMMIT to $NEW_COMMIT."

deploy_target() {
    local name="$1"
    local task_dir="$2"
    local bucket="$3"
    local credential="$4"

    if [ -r "$credential" ]; then
        echo "Deploying to $name..."
        export FIREBASE_CRED_PATH="$credential"
        export STORAGE_BUCKET="$bucket"
        node "$PLANETS_TOOLS_PATH/importProblems.js" -u "$task_dir"
        node "$PLANETS_TOOLS_PATH/uploadTestcases.js"  "$task_dir"
    fi
}

deploy_task() {
    local task_dir="$1"
    task-maker-rust --task-dir "$task_dir" --ui print
    if [ $? -ne 0 ]; then
        echo "ERROR: task-maker-rust failed for '$task_dir'."
        return 1
    fi

    deploy_target "AlgoPro" "$task_dir" "algopro-app.firebasestorage.app" "$ALGOPRO_CREDENTIAL_PATH"
    deploy_target "MATFIZ" "$task_dir" "matfiz-ide.firebasestorage.app" "$MATFIZ_CREDENTIAL_PATH"
}

git diff --name-only "$OLD_COMMIT" "$NEW_COMMIT"       \
    | awk -F/ '/^topics\// { print $1 "/" $2 "/" $3 }' \
    | sort -u                                          \
    | while read -r task_path; do
        if [ -d "$task_path" ]; then
            echo "Auto-deploying task at '$task_path'..."
            deploy_task "$task_path"
        fi
      done

echo "Deployment completed."
