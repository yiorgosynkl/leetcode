################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200514
# Problem link      : https://leetcode.com/problems/implement-trie-prefix-tree/
################################################################

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.prefices = set()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.add(word)
        for i in range(len(word) + 1):
            self.prefices.add(word[:i])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.prefices
    
# # solution by tusizi (Trie data structure)
# class TrieNode:
#     # Initialize your data structure here.
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.is_word = False

# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         current = self.root
#         for letter in word:
#             current = current.children[letter]
#         current.is_word = True

#     def search(self, word):
#         current = self.root
#         for letter in word:
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return current.is_word

#     def startsWith(self, prefix):
#         current = self.root
#         for letter in prefix:
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)