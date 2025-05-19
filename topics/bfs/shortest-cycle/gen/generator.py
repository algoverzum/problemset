#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import math
import heapq
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
    unused_nodes = list(range(1, A + 1))
    nodes = list(range(1, A + 1))
    edges = set()
    # parent itt nem direct szülőt ért, hanem, hogy melyik részfából ered.
    parent = [-1] * (A + 1)
    neighbors = [[] for _ in range(A + 1)]
    dist = [-1] * (A + 1)
    root = randint(1, A + 1)
    dist[root] = 0
    used_nodes = [root]
    unused_nodes.remove(root)
    remaining_edges = B - A + 1
    mindist = 2 * A

    # full random nem feltétlen összefüggő
    def random_graph():
        while len(edges) < B:
            u = choice(nodes)
            v = choice(nodes)
            while u == v:
                u = choice(nodes)
                v = choice(nodes)
            edge = (min(u, v), max(u, v))
            edges.add(edge)

    # random, de összefüggő
    def random_connected_graph():
        while len(edges) < B:
            u = choice(used_nodes)  # kezdetben csak root
            v = choice(nodes)
            while u == v:
                u = choice(used_nodes)
                v = choice(nodes)
            edge = (min(u, v), max(u, v))
            used_nodes.append(v)
            edges.add(edge)

    # egyenes gráf
    last_node = -1

    # ahol last node azért kell, hogy amikor ezt meghívom mert egy nagy kört szeretnék akkor csak összekötöm a last_node-ot a gyökérrel
    def line_graph(edge_param):
        nonlocal last_node
        u = root
        shuffle(unused_nodes)
        while len(edges) < edge_param:
            v = unused_nodes.pop()
            edge = (min(u, v), max(u, v))
            edges.add(edge)
            u = v
            last_node = v

    def max_cross_edges(split_nodes, M):
        """
        Két csúcs közé csak akkor húzunk élt, ha különböző részfákból valók.
        Mindig a legnagyobb dist[u] + dist[v] sum-okat választjuk.

        Paraméterek:
        dist:  {node: távolság a gyökértől}
        split_nodes: list of lists, a részfák csúcsai tetszőleges sorrendben
        M: int, hány él legyen az edges setben.

        """
        m = len(split_nodes)

        # 1) Részfák csúcsai távolság szerint csökkenő sorrendben
        nodes_sorted = [sorted(lst, key=lambda x: dist[x], reverse=True) for lst in split_nodes]

        # 2) Max-heaphez: (-(sum), p, q, ip, iq)
        heap = []
        visited = set()

        # Kezdetként minden (p,q) párból a (0,0) indexpárt toljuk
        for p in range(m):
            for q in range(p + 1, m):
                if nodes_sorted[p] and nodes_sorted[q]:
                    s = dist[nodes_sorted[p][0]] + dist[nodes_sorted[q][0]]
                    entry = (-s, p, q, 0, 0)
                    heapq.heappush(heap, entry)
                    visited.add((p, q, 0, 0))

        # 3) Iteratív "pop-push"
        while heap and len(edges) < M:
            neg_sum, p, q, ip, iq = heapq.heappop(heap)
            u = nodes_sorted[p][ip]
            v = nodes_sorted[q][iq]
            # min-max rendezés, hogy halmazban konzisztens legyen
            edges.add((min(u, v), max(u, v)))

            # Szomszédállapotok: (ip+1, iq) és (ip, iq+1)
            for dip, diq in ((1, 0), (0, 1)):
                nip, niq = ip + dip, iq + diq
                if nip < len(nodes_sorted[p]) and niq < len(nodes_sorted[q]):
                    state = (p, q, nip, niq)
                    if state not in visited:
                        visited.add(state)
                        new_sum = dist[nodes_sorted[p][nip]] + dist[nodes_sorted[q][niq]]
                        heapq.heappush(heap, (-new_sum, p, q, nip, niq))

    # random generálunk egy faszerkezetet. Aztán a gyökérből induló részfák belsejébe behúzunk random éleket hogy legyenek körök. Ezzel így nem lesz kör ami áthalad a gyökeren
    # Vagyis tudjuk kontrollálni, hogy milyen hosszú gyökeren átmenő köröket készítünk
    # Ha a részfák közé random kezdünk el éleket behúzkodni, akkor kb garantált, hogy a megoldás kis méretű kör legyen.
    # gyökeren átmenő kör hossza a két külön részfában lévő csúcs distjeinek összege+1. De sajnos ez normalizálja a két csúcs distjét a két csúcs minimum distjére.
    # dist[A]=3;dist[B]=900. akkor (A,B) 904 hosszú lesz,de dist[B]=4 lesz. És ha rakunk egy dist[C]=2;(B,C) élet akkor P gyökérnél az eddigi (P,A,B)=904 helyett lesz egy (P,A,B,C)=7 körünk.
    # Itt jön képbe a sub_tree_type
    # sub_tree_type 1:  minél kevesebb gyökeren átmenő kör és minél kevesebb részfa(normalizált elemszámmal). Ezzel garantálni tudom, hogy ne legyenek ilyen kiugró értékek mint a fenti példában.
    # sub_tree_type 2: Ez sokkal randomabb.
    def sub_tree_graph(in_edge, M, sub_tree_type):
        # Ha C=0 akkor random választunk részfa mennyiséget, hogy ne kelljen beállítgatnom mindig értéket. Egyenlőre csúcsszám gyökig.
        sub_trees = C
        if C == 0:
            if sub_tree_type == 1:
                sub_trees = randint(2, int(math.sqrt(int(math.sqrt(A)))))
            else:
                sub_trees = randint(2, int(math.sqrt(A)))
        sub_tree_parents = []

        shuffle(unused_nodes)
        for _ in range(sub_trees):
            v = unused_nodes.pop()
            used_nodes.append(v)
            sub_tree_parents.append(v)
            parent[v] = v
            edges.add((min(root, v), max(root, v)))
            neighbors[root].append(v)
            neighbors[v].append(root)
        # Már az elején szétosztjuk a csúcsokat részfákra, hogy tudjuk kontrollálni hogy milyen mélyésgekben fordulnak elő körök, vagyis élek a különböző részfák közöttt.
        if sub_tree_type == 1:
            # random elemszámú részfa helyett azonos darabszám,de van variancia mert a fákat random építem fel
            split_points = [i * (len(unused_nodes) // sub_trees) for i in range(1, sub_trees)]
        else:
            split_points = sorted(sample(range(1, len(unused_nodes)), sub_trees - 1))
        split_nodes = [unused_nodes[i:j] for i, j in zip([0] + split_points, split_points + [len(unused_nodes)])]
        # stderr.write(f"subtrees: {sub_trees}\n")
        # elősször csinálom meg a fa struktúrát aztán a részfán belüli éleket.
        for i in range(sub_trees):
            used_sub_nodes = [sub_tree_parents[i]]
            for j in range(len(split_nodes[i])):
                cs = choice(split_nodes[i])
                p = choice(used_sub_nodes)
                split_nodes[i].remove(cs)
                used_sub_nodes.append(cs)
                # dist[cs] = dist[p] + 1
                parent[cs] = sub_tree_parents[i]
                edges.add((min(p, cs), max(cs, p)))
                neighbors[p].append(cs)
                neighbors[cs].append(p)

        # belső élek
        split_nodes = [unused_nodes[i:j] for i, j in zip([0] + split_points, split_points + [len(unused_nodes)])]
        for i in range(in_edge):

            sub_tree_choice = randint(0, sub_trees - 1)
            # stderr.write(f"subtree_choice: {sub_tree_choice},splitlen: {len(split_nodes)}\n")
            u = choice(split_nodes[sub_tree_choice])
            v = choice(split_nodes[sub_tree_choice])
            e = (min(u, v), max(u, v))
            while (e in edges) or u == v:
                sub_tree_choice = randint(0, sub_trees - 1)
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
        if D != 2:
            max_cross_edges(split_nodes, M)

    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    # Type 0 full random.(valószínűleg kicsi lesz a minkör).
    # Type 1 eset nagy legkissebb körrel. Felépítem a részfákat és specifikus kereszt éleket húzok be, hogy hosszú körök legyenek.
    # Type 2 gyökérnek minden csúcs gyereke. Ezt tudom generálni a részfással.
    # Type 3 "Egyenes" gráf.
    # Type 4 gráf egy nagy kör; egyenes gráf + egy él
    # Type 5 Nincs kör. csak nem húzok be kereszt élt.
    # type 6 random de összefüggő

    # full random nem feltétlen összefüggő
    if D == 0:
        random_graph()
    elif D == 1:
        inedge = int(0.99 * (B - A + 1))
        cedge = B - A + 1 - inedge
        sub_tree_graph(inedge, B, 1)
    elif D == 2:
        assert C == A - 1
        assert B == A - 1
        sub_tree_graph(0, 0, 1)
    elif D == 3:
        assert B == A - 1
        line_graph(B)
    elif D == 4:
        assert B == A
        line_graph(B - 1)
        edges.add((min(root, last_node), max(root, last_node)))
    elif D == 5:
        sub_tree_graph(B - A + 1, B, 1)
    elif D == 6:
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
