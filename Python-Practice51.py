# Day 12 - 45: Trie Data Structure
class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            node = node.children.setdefault(ch, Node())
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def words_with_prefix(self, prefix):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return []
            node = node.children[ch]
        result = []
        def collect(cur, suffix):
            if cur.end:
                result.append(prefix.lower() + suffix)
            for ch, child in cur.children.items():
                collect(child, suffix + ch)
        collect(node, "")
        return result

    def count_words(self):
        def count(node):
            return int(node.end) + sum(count(c) for c in node.children.values())
        return count(self.root)

    def delete(self, word):
        def remove(node, i):
            if i == len(word):
                if not node.end:
                    return False
                node.end = False
                return True
            ch = word[i]
            if ch not in node.children:
                return False
            deleted = remove(node.children[ch], i + 1)
            child = node.children[ch]
            if deleted and not child.end and not child.children:
                del node.children[ch]
            return deleted
        return remove(self.root, 0)

trie = Trie()

# 1. Insert words
for word in ["apple", "app", "apply", "apt", "banana", "bat", "ball"]:
    trie.insert(word)
print("1. Words inserted")

# 2. Exact search
print("2. Search apple:", trie.search("apple"))

# 3. Search missing word
print("3. Search orange:", trie.search("orange"))

# 4. Prefix check
print("4. Prefix app:", trie.starts_with("app"))

# 5. Autocomplete
print("5. Words starting with ap:", trie.words_with_prefix("ap"))

# 6. Count words
print("6. Word count:", trie.count_words())

# 7. Delete word
print("7. Delete apt:", trie.delete("apt"))

# 8. Verify deletion
print("8. Search apt:", trie.search("apt"))

# 9. Add another word
trie.insert("application")
print("9. Autocomplete app:", trie.words_with_prefix("app"))

# 10. Final count
print("10. Final count:", trie.count_words())
