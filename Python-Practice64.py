# 57_segment_tree.py
# Segment Tree - 10 practical programs/features

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * max(1, self.n))
        self.data = list(data)
        if self.n:
            self._build(1, 0, self.n - 1)

    def _build(self, node, left, right):
        if left == right:
            self.tree[node] = self.data[left]
            return
        mid = (left + right) // 2
        self._build(node * 2, left, mid)
        self._build(node * 2 + 1, mid + 1, right)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query_sum(self, ql, qr):
        if not self.n or ql < 0 or qr >= self.n or ql > qr:
            raise ValueError("Invalid range")
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, left, right, ql, qr):
        if ql <= left and right <= qr:
            return self.tree[node]
        mid = (left + right) // 2
        total = 0
        if ql <= mid:
            total += self._query(node * 2, left, mid, ql, qr)
        if qr > mid:
            total += self._query(node * 2 + 1, mid + 1, right, ql, qr)
        return total

    def update(self, index, value):
        if not 0 <= index < self.n:
            raise IndexError("Index out of range")
        self.data[index] = value
        self._update(1, 0, self.n - 1, index, value)

    def _update(self, node, left, right, index, value):
        if left == right:
            self.tree[node] = value
            return
        mid = (left + right) // 2
        if index <= mid:
            self._update(node * 2, left, mid, index, value)
        else:
            self._update(node * 2 + 1, mid + 1, right, index, value)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]


# 1. Build a tree
data = [2, 4, 6, 8, 10]
st = SegmentTree(data)
print("1. Built tree:", st.tree[1:2 * len(data)])

# 2. Range sum
print("2. Sum [1, 3]:", st.query_sum(1, 3))

# 3. Point update
st.update(2, 20)
print("3. After update:", st.data)

# 4. Range sum after update
print("4. New sum [1, 3]:", st.query_sum(1, 3))

# 5. Prefix sum using the segment tree
print("5. Prefix sum [0, 2]:", st.query_sum(0, 2))

# 6. Single-element query
print("6. Single element [3, 3]:", st.query_sum(3, 3))

# 7. Whole-array query
print("7. Whole array:", st.query_sum(0, len(data) - 1))

# 8. Multiple updates
for i, value in [(0, 5), (4, 25)]:
    st.update(i, value)
print("8. Multiple updates:", st.data)

# 9. Multiple range queries
for left, right in [(0, 1), (2, 4), (1, 4)]:
    print(f"9. Sum [{left}, {right}]:", st.query_sum(left, right))

# 10. Complexity note
print("10. Feature: range query and point update are O(log n).")
