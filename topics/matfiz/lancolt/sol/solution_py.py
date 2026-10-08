#!/usr/bin/env python3
# @check-accepted: *


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def beszur_eleje(head, ertek):
    uj = Node(ertek)
    uj.next = head
    return uj


def beszur_utan(p, ertek):
    if p is None:
        return
    uj = Node(ertek)
    uj.next = p.next
    p.next = uj


def rendezett_beszur(head, ertek):
    # Üres lista vagy elejére kell beszúrni
    if head is None or ertek < head.data:
        return beszur_eleje(head, ertek)

    # Megkeressük azt az elemet, amely után be kell szúrni
    p = head
    while p.next is not None and p.next.data < ertek:
        p = p.next

    # Beszúrás p után
    beszur_utan(p, ertek)
    return head


def kiir(head):
    p = head
    while p is not None:
        print(p.data, end=" ")
        p = p.next
    print()


def main():
    head = None
    n = int(input())
    szamok = list(map(int, input().split()))

    for x in szamok:
        head = rendezett_beszur(head, x)

    kiir(head)


if __name__ == "__main__":
    main()

"""
alternatív megoldás

def main():
    n = int(input())
    szamok = list(map(int, input().split()))
    szamok.sort()
    print(' '.join(map(str, szamok)))

if __name__ == "__main__":
    main()
"""
