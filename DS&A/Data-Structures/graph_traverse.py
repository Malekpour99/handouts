# BFS: Breadth First Search -> Queue
# DFS: Depth First Search -> Stack


def bfs(G: dict, s: str = "0", v: list = []):
    """Searching graph(G) - which is a dictionary - starting from (s) vertex
    including visited vertices in (v) list; using BFS method"""
    q = []
    v.append(s)
    q.append(s)
    while q:
        m = q.pop(0)
        print(m, end=" ")
        for n in G[m]:
            if n not in v:
                v.append(n)
                q.append(n)


g = {
    "0": ["1", "2"],
    "1": ["3", "4", "6"],
    "2": ["5", "6"],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
}

bfs(g)  # 0 1 2 3 4 6 5
print()


def dfs(G: dict, s: str = "0", v: list = []):
    """Searching graph(G) - which is a dictionary - starting from (s) vertex
    including visited vertices in (v) list; using DFS method"""
    if s not in v:
        print(s, end=" ")
        v.append(s)
        for n in G[s]:
            dfs(G, n, v)


dfs(g)  # 0 1 3 4 6 2 5
