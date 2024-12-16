class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Sample Workouts
trie = Trie()
words = ["apple", "app", "banana", "bat", "bar"]
for word in words:
    trie.insert(word)

print("Search for 'apple':", trie.search("apple"))  # True
print("Search for 'appl':", trie.search("appl"))  # False
print("Prefix search for 'app':", trie.starts_with("app"))  # True
print("Prefix search for 'bat':", trie.starts_with("bat"))  # True
