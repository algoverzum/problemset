#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import math
from collections import deque
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "shortest-cycle".

Parameters:
* A (N)
* B (M)
* C (number of subtrees)
* D (type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
* %d <= D <= %d
""" % (
    MIN,
    MAX,
    MIN2,
    MAX2,
    0,
    MAX - 1,
    0,
    6,
)


def run(A, B, C, D):
    unused_nodes = list(range(A))
    nodes = list(range(A))
    edges = set()
    parent = [-1] * (A + 1)
    neighbors = [] * (A + 1)
    dist = [-1] * (A + 1)
    root = 1
    dist[root] = 0
    used_nodes = [root]
    unused_nodes.remove(root)
    remaining_edges = B - A + 1
    mindist = 2 * A

    # full random nem feltétlen összefüggő
    def random_graph():
        edge_count = 0
        while edge_count < B:
            u = choice(nodes)
            v = choice(nodes)
            edge = (min(u, v), max(u, v))
            while edge in edges:
                u = choice(nodes)
                v = choice(nodes)
                edge = (min(u, v), max(u, v))
            edge_count += 1
            edges.add(edge)

    # random, de összefüggő
    def random_connected_graph():
        edge_count = 0
        while edge_count < B:
            u = choice(used_nodes)
            v = choice(nodes)
            edge = (min(u, v), max(u, v))
            while edge in edges:
                u = choice(used_nodes)
                v = choice(nodes)
                edge = (min(u, v), max(u, v))
            used_nodes.append(v)
            edge_count += 1
            edges.add(edge)

    # egyenes gráf
    last_node = -1

    def line_graph():
        edge_count = 0
        u = root
        while edge_count < B - 1:
            v = choice(unused_nodes)
            edge = (min(u, v), max(u, v))
            while edge in edges:
                v = choice(unused_nodes)
                edge = (min(u, v), max(u, v))
            edge_count = edge_count + 1
            edges.add(edge)
            unused_nodes.remove(v)
            u = v
            last_node = v

    # random generálunk egy faszerkezetet. Aztán a gyökérből induló részfák belsejébe behúzunk random éleket hogy legyenek körök. Ezzel így nem lesz kör ami áthalad a gyökeren
    # Vagyis tudjuk kontrollálni, hogy milyen hosszú gyökeren átmenő köröket készítünk
    # Ha a részfák közé random kezdünk el éleket behúzkodni, akkor kb garantált, hogy a megoldás kis méretű kör legyen.
    # gyökeren átmenő kör hossza a két külön részfában lévő csúcs distjeinek összege+1. De sajnos ez normalizálja a két csúcs distjét a két csúcs minimum distjére.
    # dist[A]=3;dist[B]=900. akkor (A,B) 904 hosszú lesz,de dist[B]=4 lesz. És ha rakunk egy dist[C]=2;(B,C) élet akkor P gyökérnél az eddigi (P,A,B)=904 helyett lesz egy (P,A,B,C)=7 körünk.
    # Itt jön képbe a sub_tree_type
    # sub_tree_type 1:  minél kevesebb gyökeren átmenő kör és minél kevesebb részfa(normalizált darabszámmal). Ezzel garantálni tudom, hogy ne legyenek ilyen kiugró értékek mint a fenti példában.
    # És mohózom a leghosszabb köröket
    # sub_tree_type 2: Ez sokkal randomabb viszont ahelyett hogy mohóznám a max körhosszt. helyette hasonló distü csúcsokat párosítok és így akadályozom meg hogy kis kör legyen.
    # itt az a feltevésem hogy hosszab kört generál mint full random gráf, de rövidebbet mint a sub_tree_type 1.
    def sub_tree_graph(in_edge, cross_edge, sub_tree_type):
        # Ha C=0 akkor random választunk részfa mennyiséget, hogy ne kelljen beállítgatnom mindig értéket. Egyenlőre csúcsszám gyökig.
        sub_trees = C
        if C == 0:
            if sub_tree_type == 1:
                sub_trees = randint(2, int(math.sqrt(int(math.sqrt(A)))))
            else:
                sub_trees = randint(2, int(math.sqrt(A)))
        sub_tree_parents = []

        for _ in range(sub_trees):
            v = choice(unused_nodes)
            unused_nodes.remove(v)
            used_nodes.append(v)
            sub_tree_parents.append(v)
            # dist[v] = 1
            # parent[v] = root
            edges.add((min(root, v), max(root, v)))
            neighbors[root].append(v)
            neighbors[v].append(root)
        # Már az elején szétosztjuk a csúcsokat részfákra, hogy tudjuk kontrollálni hogy milyen mélyésgekben fordulnak elő körök, vagyis élek a különböző részfák közöttt.
        shuffle(unused_nodes)
        if sub_tree_type == 1:
            split_points = [i * (len(unused_nodes) // sub_trees) for i in range(1, sub_trees)]
        else:
            split_points = sorted(sample(range(1, len(unused_nodes)), sub_trees - 1))
        split_nodes = [unused_nodes[i:j] for i, j in zip([0] + split_points, split_points + [len(unused_nodes)])]

        # elősször csinálom meg a fa struktúrát aztán a részfán belüli éleket.
        for i in range(sub_trees):
            used_sub_nodes = [sub_tree_parents[i]]
            for j in range(len(split_nodes[i])):
                cs = choice(split_nodes[i])
                p = choice(used_sub_nodes)
                split_nodes[i].remove(cs)
                used_sub_nodes.append(cs)
                # dist[cs] = dist[p] + 1
                # parent[cs] = p
                edges.add((min(p, cs), max(cs, p)))
                neighbors[p].append(cs)
                neighbors[cs].append(p)

        # belső élek
        for i in range(in_edge):
            sub_tree_choice = randint(sub_trees)
            u = choice(split_nodes[sub_tree_choice])
            v = choice(split_nodes[sub_tree_choice])
            e = (min(u, v), max(u, v))
            while e in edges:
                sub_tree_choice = randint(sub_trees)
                u = choice(split_nodes[sub_tree_choice])
                v = choice(split_nodes[sub_tree_choice])
                e = (min(u, v), max(u, v))
            edges.add(e)
            neighbors[u].append(v)
            neighbors[v].append(u)

        # bfs dist számolásért
        q = deque([root])
        dist[root] = 0
        while q:
            node = q.popleft()
            for n in neighbors[node]:
                if dist[n] == -1:
                    dist[n] = dist[node] + 1
                    q.append(n)

        # minden sub-tree csúcsai csökkenő sorrendben
        nodes_sorted = [sorted(lst, key=lambda x: dist[x], reverse=True) for lst in split_nodes]
        # a subtreek hanyadik legnagyobb dist-ü csúcsánál járunk
        node_pointers = [0] * sub_trees
        # minden sub-tree node pointeredik csúcsa, csökkenő sorrendben
        Y = sorted(
            [nodes_sorted[i][node_pointers[i]] for i in range(sub_trees) if node_pointers[i] < len(nodes_sorted[i])],
            key=lambda x: dist[x],
            reverse=True,
        )

        P1, P2 = 0, 1
        for j in range(cross_edge):
            u, v = Y[P1], Y[P2]
            edges.add((min(u, v), max(u, v)))
            neighbors[u].append(v)
            neighbors[v].append(u)
            dist[u] = min(dist[u], dist[v] + 1)

    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    # Type 0 full random.(valószínűleg kicsi lesz a minkör).
    # Type 1 eset nagy legkissebb körrel. Felépítem a részfákat és specifikus kereszt éleket húzok be, hogy hosszú körök legyenek.
    # Type 2 gyökérnek minden csúcs gyereke. Ezt tudom generálni a részfással.
    # Type 3 "Egyenes" gráf.
    # Type 4 gráf egy nagy kör. egyenes gráf speceset
    # Type 5 Nincs kör. csak nem húzok be kereszt élt.
    # type 6 random de összefüggő

    # full random nem feltétlen összefüggő
    match D:
        case 0:
            random_graph()
        case 1:
            sub_tree_graph()
        case 2:
            sub_tree_graph(0, 0, 1)
        case 3:
            B = A - 1
            line_graph()
        case 4:
            B = A
            line_graph()
            edges.add((min(root, last_node), max(root, last_node)))
        case 5:
            sub_tree_graph(B - A + 1, 0, 1)
        case 6:
            random_connected_graph()

    print(A, B, root)
    edges_list = list(edges)
    shuffle(edges_list)
    for u, v in edges_list:
        if choice([True, False]):
            print(u, v)
        else:
            print(v, u)


if __name__ == "__main__":
    num_args = len(signature(run).parameters) + 2
    if len(argv) != num_args:
        print("Got %d parameters, expecting %d" % (len(argv), num_args), file=stderr)
        print(usage, file=stderr)
        exit(1)

    def tryconv(x):
        for t in [int, float, str]:
            try:
                return t(x)
            except:
                pass

    *args, S = map(tryconv, argv[1:])
    seed(S)
    run(*args)
