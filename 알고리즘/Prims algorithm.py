from collections import defaultdict
import heapq

def mst():
    V, E = 6, 9
    edges = [[1, 2, 6], [1, 3, 3], [2, 3, 2], [2, 4, 5], [3, 4, 3], [3, 5, 4], [4, 5, 2], [4, 6, 3], [5, 6, 5]]

    graph = defaultdict(list)
    for srt, dst, weight in edges:
        graph[srt].append((dst, weight))
        graph[dst].append((srt, weight))

    mst_graph = [[0] * V for _ in range(V)]
    mst_nodes = [-1 for _ in range(V)]
    visited = [True for _ in range(V)]
    q = [(0, 1, 1)]
    while q:
        cost, node, prev = heapq.heappop(q)
        if visited[node - 1] is False:
            continue
        visited[node - 1] = False
        mst_graph[node - 1][prev - 1] = 1
        mst_graph[prev - 1][node - 1] = 1
        mst_nodes[node - 1] = cost
        for dst, weight in graph[node]:
            if visited[dst - 1] is True:
                heapq.heappop(q, (weight, dst, node))
    print('MST cost is {sum(mst_nodes)}')
    mst_graph[0][0] = 1
    for row in mst_graph:
        print(*row)

mst()
