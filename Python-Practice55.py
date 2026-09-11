"""49 - Union-Find / Disjoint Set: 10 practical programs"""

def make_dsu(n):
    parent, rank = list(range(n)), [0] * n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        if rank[a] < rank[b]: a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]: rank[a] += 1
        return True
    return find, union

# 1. Singleton sets
find, union = make_dsu(5)
print("1.", [find(i) for i in range(5)])

# 2. Union two elements
union(0, 1)
print("2. Connected:", find(0) == find(1))

# 3. Connected components
def component_count(n, edges):
    find, union = make_dsu(n)
    count = n
    for a, b in edges:
        if union(a, b): count -= 1
    return count
print("3.", component_count(6, [(0,1),(1,2),(3,4)]))

# 4. Cycle detection
def has_cycle(n, edges):
    find, union = make_dsu(n)
    return any(not union(a, b) for a, b in edges)
print("4.", has_cycle(4, [(0,1),(1,2),(2,3),(3,0)]))

# 5. Connectivity check
print("5.", component_count(4, [(0,1),(1,2),(2,3)]) == 1)

# 6. Friend groups
def friend_groups(n, friendships):
    find, union = make_dsu(n)
    for a, b in friendships: union(a, b)
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    return list(groups.values())
print("6.", friend_groups(7, [(0,1),(1,2),(3,4),(5,6)]))

# 7. Merge accounts by shared email
def merge_accounts(accounts):
    find, union = make_dsu(len(accounts))
    owner = {}
    for i, emails in enumerate(accounts):
        for email in emails:
            if email in owner: union(i, owner[email])
            else: owner[email] = i
    groups = {}
    for i, emails in enumerate(accounts):
        groups.setdefault(find(i), set()).update(emails)
    return [sorted(v) for v in groups.values()]
print("7.", merge_accounts([["a@x.com","b@x.com"],["b@x.com","c@x.com"],["z@x.com"]]))

# 8. Number of islands from adjacent land cells
def island_count(cells):
    cells = set(cells)
    find, union = make_dsu(len(cells))
    ids = {cell:i for i, cell in enumerate(cells)}
    for r,c in cells:
        for nb in [(r+1,c),(r,c+1)]:
            if nb in ids: union(ids[(r,c)], ids[nb])
    return len({find(i) for i in range(len(cells))})
print("8.", island_count([(0,0),(0,1),(2,2),(2,3)]))

# 9. Extra edge that creates a cycle
def redundant_edge(n, edges):
    find, union = make_dsu(n)
    for edge in edges:
        if not union(*edge): return edge
print("9.", redundant_edge(3, [(0,1),(1,2),(0,2)]))

# 10. Kruskal connectivity helper
print("10.", component_count(5, [(0,1),(1,2),(2,3),(3,4)]))
