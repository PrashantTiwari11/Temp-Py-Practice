# 53 - AVL Tree: 10 practical programs

class Node:
    def __init__(self, key):
        self.key, self.left, self.right, self.height = key, None, None, 1

def h(n): return n.height if n else 0
def update(n): n.height = 1 + max(h(n.left), h(n.right))
def rotate_right(y):
    x, t = y.left, y.left.right
    x.right, y.left = y, t
    update(y); update(x)
    return x
def rotate_left(x):
    y, t = x.right, x.right.left
    y.left, x.right = x, t
    update(x); update(y)
    return y

# 1. Insert with AVL balancing
def insert(root, key):
    if not root: return Node(key)
    if key < root.key: root.left = insert(root.left, key)
    elif key > root.key: root.right = insert(root.right, key)
    else: return root
    update(root)
    b = h(root.left) - h(root.right)
    if b > 1 and key < root.left.key: return rotate_right(root)
    if b < -1 and key > root.right.key: return rotate_left(root)
    if b > 1 and key > root.left.key:
        root.left = rotate_left(root.left); return rotate_right(root)
    if b < -1 and key < root.right.key:
        root.right = rotate_right(root.right); return rotate_left(root)
    return root

# 2. Inorder traversal
def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

# 3. Preorder traversal
def preorder(root):
    return [root.key] + preorder(root.left) + preorder(root.right) if root else []

# 4. Search
def search(root, key):
    if not root or root.key == key: return root
    return search(root.left, key) if key < root.key else search(root.right, key)

# 5. Minimum value
def minimum(root):
    while root.left: root = root.left
    return root.key

# 6. Maximum value
def maximum(root):
    while root.right: root = root.right
    return root.key

# 7. Count nodes
def count_nodes(root):
    return 0 if not root else 1 + count_nodes(root.left) + count_nodes(root.right)

# 8. Tree height
def tree_height(root): return h(root)

# 9. Check AVL balance
def balanced(root):
    if not root: return True
    return abs(h(root.left)-h(root.right)) <= 1 and balanced(root.left) and balanced(root.right)

# 10. Build and test AVL tree
root = None
for value in [30, 20, 10, 25, 28, 40, 50]:
    root = insert(root, value)

print("1. Inorder:", inorder(root))
print("2. Preorder:", preorder(root))
print("3. Search 28:", search(root, 28) is not None)
print("4. Minimum:", minimum(root))
print("5. Maximum:", maximum(root))
print("6. Node count:", count_nodes(root))
print("7. Height:", tree_height(root))
print("8. Balanced:", balanced(root))
print("9. Root:", root.key)
print("10. Search 99:", search(root, 99) is not None)
