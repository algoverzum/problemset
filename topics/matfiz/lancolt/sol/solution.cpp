// @check-accepted: *
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next;
};

// Beszúrás a lista elejére
void beszur_eleje(Node *&head, int ertek) {
    Node *uj = new Node;

    uj->data = ertek;
    uj->next = head;

    head = uj;
}

// Beszúrás egy adott elem után
void beszur_utan(Node *p, int ertek) {
    if (p == nullptr)
        return;

    Node *uj = new Node;

    uj->data = ertek;

    uj->next = p->next;
    p->next = uj;
}

// Rendezett beszúrás
void rendezett_beszur(Node *&head, int ertek) {

    // Üres lista vagy elejére kell beszúrni
    if (head == nullptr || ertek < head->data) {
        beszur_eleje(head, ertek);
        return;
    }

    // Megkeressük azt az elemet, amely után be kell szúrni
    Node *p = head;
    while (p->next != nullptr && p->next->data < ertek) {
        p = p->next;
    }
    // Beszúrás p után
    beszur_utan(p, ertek);
}

// Lista kiírása
void kiir(Node *head) {

    Node *p = head;
    while (p != nullptr) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

int main() {

    Node *head = nullptr;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        rendezett_beszur(head, x);
    }
    kiir(head);
    return 0;
}

/*alternatív megoldás:

#include <iostream>
#include <list>

using namespace std;

int main() {

    list<int> lista;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {

        int x;
        cin >> x;

        // Megkeressük az első olyan elemet,
        // amely nem kisebb x-nél
        list<int>::iterator it = lista.begin();

        while (it != lista.end() && *it < x) {
            ++it;
        }

        // Beszúrás a megfelelő helyre
        lista.insert(it, x);
    }

    // Kiírás
    for (int x : lista) {
        cout << x << " ";
    }

    cout << endl;

    return 0;
}

*/