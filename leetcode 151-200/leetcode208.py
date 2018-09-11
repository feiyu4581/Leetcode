class Node:
    def __init__(self, val):
        self.val = val
        self.childs = {}
        self._is_word = False

    def next(self, char):
        if char not in self.childs:
            self.childs[char] = Node(char)

        return self.childs[char]

    def search(self, char):
        return char in self.childs

    def is_word(self):
        return self._is_word

    def set_word(self):
        self._is_word = True


class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('root')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            current = current.next(char)

        current.set_word()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if not current.search(char):
                return False

            current = current.next(char)

        return current.is_word()
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if not current.search(char):
                return False

            current = current.next(char)

        return True
        

trie = Trie()

trie.insert("apple")
print(trie.search("apple") == True)
print(trie.search("app") == False)
print(trie.startsWith("app") == True)
trie.insert("app")   
print(trie.search("app") == True)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)