# 62_binary_search_tree.py
# Binary Search Tree - 10 practical programs/features

class Node:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

def insert(root, value):
    if root is None: return Node(value)
    if value < root.value: root.left = insert(root.left, value)
    elif value > root.value: root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value: return root
    return search(root.left, value) if value < root.value else search(root.right, value)

def inorder(root, out=None):
    out = [] if out is None else out
    if root:
        inorder(root.left, out); out.append(root.value); inorder(root.right, out)
    return out

def preorder(root, out=None):
    out = [] if out is None else out
    if root:
        out.append(root.value); preorder(root.left, out); preorder(root.right, out)
    return out

def postorder(root, out=None):
    out = [] if out is None else out
    if root:
        postorder(root.left, out); postorder(root.right, out); out.append(root.value)
    return out

def height(root):
    return 0 if root is None else 1 + max(height(root.left), height(root.right))

def delete(root, value):
    if root is None: return None
    if value < root.value: root.left = delete(root.left, value)
    elif value > root.value: root.right = delete(root.right, value)
    else:
        if root.left is None: return root.right
        if root.right is None: return root.left
        s = root.right
        while s.left: s = s.left
        root.value = s.value
        root.right = delete(root.right, s.value)
    return root

root = None
for x in [50,30,70,20,40,60,80]: root = insert(root, x)
print("1. BST created:", inorder(root))
root = insert(root, 65)
print("2. Insert 65:", inorder(root))
print("3. Search 40:", search(root, 40) is not None)
print("4. Search 99:", search(root, 99) is not None)
print("5. Inorder:", inorder(root))
print("6. Preorder:", preorder(root))
print("7. Postorder:", postorder(root))
print("8. Height:", height(root))
print("9. Min/Max:", min(inorder(root)), max(inorder(root)))
root = delete(root, 30)
print("10. Delete 30:", inorder(root))
