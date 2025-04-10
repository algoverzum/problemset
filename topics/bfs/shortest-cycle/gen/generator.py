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

    # random generálunk egy faszerkezetet. Aztán a gyökérből induló részfák belsejébe behúzunk random éleket hogy legyenek körök. Ezzel így nem lesz kör ami áthalad a gyökeren
    # Vagyis tudjuk kontrollálni, hogy milyen hosszú gyökeren átmenő köröket készítünk
    # Ha a részfák közé random kezdünk el éleket behúzkodni, akkor kb garantált, hogy a megoldás kis méretű kör legyen.
    # gyökeren átmenő kör hossza a két külön részfában lévő csúcs distjeinek összege+1. De sajnos ez normalizálja a két csúcs distjét a két csúcs minimum distjére.
    # dist[A]=3;dist[B]=900. akkor (A,B) 904 hosszú lesz,de dist[B]=4 lesz. És ha rakunk egy dist[C]=2;(B,C) élet akkor P gyökérnél az eddigi (P,A,B)=904 helyett lesz egy (P,A,B,C)=7 körünk.
    # Itt jön képbe a sub_tree_type
    # sub_tree_type 1:  minél kevesebb gyökeren átmenő kör és minél kevesebb részfa(normalizált elemszámmal). Ezzel garantálni tudom, hogy ne legyenek ilyen kiugró értékek mint a fenti példában.
    # sub_tree_type 2: Ez sokkal randomabb.
    def sub_tree_graph(in_edge, cross_edge, sub_tree_type):
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
        """ Proof of concept
        részfák(van belső kör már fákban szóval részgráf)
        fa1: 10,10,9 8, 8, 7
        fa2: 10,9,9,9,8,
        fa3: 9,8,8,8,7
        fa4: 7,6,5,4
        sorted_nodes:      x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x,
        dist[sorted_nodes]:10,10,10,9,9,9,9,8,8,8....
        value_start:0,3,7,13
        1.legnagyobb összeg value_start[0]+value_start[0]
        2. legnagyobb.  value_start[0]+value_start[1]
        3. legnagyobb.  value_start[0]+value_start[2] Vagy value_start[1]+value_start[1]
        
        összegek alapján megyek sorba
        n. legnagyobb value_start[a]+value_start[b].   a+b=n-1
        currentsum=n-1
        start_a=a, start_b=b                         0,1
        start_a_index=value_start[a],start_b_index   0,3
        a_node=sorted_nodes[value_start[a]]         x0,x3
        dist_a=dist[P1],dist_b=dist[P2]              10,9                        
        """

        sorted_nodes = sorted(nodes, key=lambda x: dist[x], reverse=True)
        maxdist = dist[sorted_nodes[0]]
        value_start_index = [0]
        if True:
            bigcycles = 0
            lastvalue = maxdist
            valuecount = 0
            # value_start_index[0] = 0
            currentsum = 0
            # stderr.write(f"distlen: {len(dist)}, sorted_nodes_len: {len(sorted_nodes)}\n")
            for k in range(len(dist) - 1):
                if dist[sorted_nodes[k]] != lastvalue:
                    lastvalue = dist[sorted_nodes[k]]
                    valuecount = valuecount + 1
                    # stderr.write(f"dist: {dist[sorted_nodes[k]]}, lastvalue: {lastvalue}\n")
                    value_start_index.append(k)
            while bigcycles <= cross_edge:
                for j in range((currentsum + 1) // 2):
                    if bigcycles == cross_edge:
                        return
                    start_a = j
                    start_b = currentsum - j
                    start_a_index = value_start_index[start_a]
                    start_b_index = value_start_index[start_b]
                    a_node = sorted_nodes[start_a_index]
                    b_node = sorted_nodes[start_b_index]
                    dist_a = dist[a_node]
                    dist_b = dist[b_node]
                    for P1 in range(value_start_index[start_a], value_start_index[start_a + 1]):
                        for P2 in range(value_start_index[start_b], value_start_index[start_b + 1]):
                            a_node = sorted_nodes[P1]
                            b_node = sorted_nodes[P2]
                            if bigcycles == cross_edge:
                                return
                            if parent[a_node] != parent[b_node]:
                                e = (min(a_node, b_node), max(a_node, b_node))
                                edges.add(e)
                                bigcycles = bigcycles + 1
                # Amikor value_start[a]+value_start[a] eset van.
                if currentsum % 2 == 0:
                    start_a = currentsum // 2
                    for P1 in range(value_start_index[start_a], value_start_index[start_a + 1]):
                        for P2 in range(P1, value_start_index[start_a + 1]):
                            a_node = sorted_nodes[P1]
                            b_node = sorted_nodes[P2]
                            if bigcycles == cross_edge:
                                return
                            if parent[a_node] != parent[b_node]:
                                e = (min(a_node, b_node), max(a_node, b_node))
                                edges.add(e)
                                bigcycles = bigcycles + 1
                currentsum = currentsum + 1

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
    match D:
        case 0:
            random_graph()
        case 1:
            inedge = int(0.99 * (B - A + 1))
            cedge = B - A + 1 - inedge
            sub_tree_graph(inedge, cedge, 1)
        case 2:
            assert C == A - 1
            assert B == A - 1
            sub_tree_graph(0, 0, 1)
        case 3:
            assert B == A - 1
            line_graph(B)
        case 4:
            assert B == A
            line_graph(B - 1)
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
