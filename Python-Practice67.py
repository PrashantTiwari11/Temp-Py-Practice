# 61_graph_algorithms.py
# Graph Algorithms - 10 practical programs/features
from collections import deque

def bfs(graph, start):
    seen, order, q = {start}, [], deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)
    return order

def dfs(graph, start):
    seen, order = set(), []
    def visit(node):
        seen.add(node); order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen: visit(nxt)
    visit(start)
    return order

def dijkstra(graph, start):
    dist = {n: float("inf") for n in graph}; dist[start] = 0
    remaining = set(graph)
    while remaining:
        node = min(remaining, key=dist.get); remaining.remove(node)
        for nxt, weight in graph[node]:
            dist[nxt] = min(dist[nxt], dist[node] + weight)
    return dist

def components(graph):
    seen, result = set(), []
    for node in graph:
        if node not in seen:
            part = bfs(graph, node); seen.update(part); result.append(part)
    return result

def has_cycle(graph):
    seen = set()
    def visit(node, parent):
        seen.add(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                if visit(nxt, node): return True
            elif nxt != parent: return True
        return False
    return any(visit(n, None) for n in graph if n not in seen)

g = {"A":["B","C"], "B":["A","D"], "C":["A","D"], "D":["B","C"]}
print("1. Graph:", g)
print("2. BFS:", bfs(g, "A"))
print("3. DFS:", dfs(g, "A"))
print("4. Components:", components(g))
print("5. Has cycle:", has_cycle(g))
wg = {"A":[("B",4),("C",2)], "B":[("D",5)], "C":[("B",1),("D",8)], "D":[]}
print("6. Weighted graph:", wg)
print("7. Dijkstra:", dijkstra(wg, "A"))
print("8. Degree of A:", len(g["A"]))
g["E"] = ["A"]; g["A"].append("E")
print("9. Added E:", g)
g["A"].remove("E"); g["E"].remove("A")
print("10. Removed E:", g)
