# 55 - Advanced Graph BFS/DFS: 10 practical programs
from collections import deque

GRAPH = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2,4], 4:[3]}

# 1. BFS traversal
def bfs(graph, start):
    q, seen, order = deque([start]), {start}, []
    while q:
        u = q.popleft(); order.append(u)
        for v in graph.get(u, []):
            if v not in seen: seen.add(v); q.append(v)
    return order
print("1. BFS:", bfs(GRAPH, 0))

# 2. DFS traversal
def dfs(graph, start):
    seen, order = set(), []
    def visit(u):
        seen.add(u); order.append(u)
        for v in graph.get(u, []):
            if v not in seen: visit(v)
    visit(start)
    return order
print("2. DFS:", dfs(GRAPH, 0))

# 3. Shortest distance in an unweighted graph
def shortest_distance(graph, start, target):
    q, dist = deque([(start,0)]), {start}
    while q:
        u, d = q.popleft()
        if u == target: return d
        for v in graph.get(u, []):
            if v not in dist: dist.add(v); q.append((v,d+1))
    return -1
print("3. Distance:", shortest_distance(GRAPH, 0, 4))

# 4. Connected components
def component_count(graph):
    seen, count = set(), 0
    for start in graph:
        if start in seen: continue
        count += 1; stack = [start]
        while stack:
            u = stack.pop()
            if u in seen: continue
            seen.add(u); stack.extend(graph.get(u, []))
    return count
print("4. Components:", component_count({0:[1],1:[0],2:[3],3:[2],4:[]}))

# 5. Cycle detection in undirected graph
def has_cycle(graph):
    seen = set()
    def visit(u, parent):
        seen.add(u)
        for v in graph.get(u, []):
            if v not in seen:
                if visit(v, u): return True
            elif v != parent: return True
        return False
    return any(visit(u, None) for u in graph if u not in seen)
print("5. Cycle:", has_cycle(GRAPH))

# 6. Bipartite graph check
def is_bipartite(graph):
    color = {}
    for start in graph:
        if start in color: continue
        color[start] = 0; q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in color: color[v] = 1-color[u]; q.append(v)
                elif color[v] == color[u]: return False
    return True
print("6. Bipartite:", is_bipartite({0:[1,3],1:[0,2],2:[1,3],3:[0,2]}))

# 7. Topological sorting
def topo(graph):
    indegree = {u:0 for u in graph}
    for u in graph:
        for v in graph[u]: indegree[v] = indegree.get(v,0)+1
    q = deque(u for u in indegree if indegree[u] == 0); order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0: q.append(v)
    return order if len(order) == len(indegree) else None
print("7. Topological:", topo({0:[1,2],1:[3],2:[3],3:[]}))

# 8. Path existence
def path_exists(graph, start, target): return target in bfs(graph, start)
print("8. Path 0->4:", path_exists(GRAPH,0,4))

# 9. BFS level map
def levels(graph, start):
    dist = {start:0}; q = deque([start])
    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v not in dist: dist[v] = dist[u]+1; q.append(v)
    return dist
print("9. Levels:", levels(GRAPH,0))

# 10. All paths in a DAG
def all_paths(graph, start, target):
    result = []
    def go(u, path):
        if u == target: result.append(path); return
        for v in graph.get(u, []): go(v, path+[v])
    go(start,[start])
    return result
print("10. All paths:", all_paths({0:[1,2],1:[3],2:[3],3:[]},0,3))
