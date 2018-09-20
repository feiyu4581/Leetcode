class Node:
    def __init__(self, val):
        self.val = val
        self.childs = {}
        self.is_word = False

    def add(self, char):
        if char not in self.childs:
            self.childs[char] = Node(char)

        return self.childs[char]

    def set_word(self):
        self.is_word = True

    def search(self, char):
        if char in self.childs:
            return [self.childs[char]]

        if char == '.':
            return self.childs.values()

        return []


class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('root')
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            current = current.add(char)

        current.set_word()


    def _search(self, word, index, node):
        if index == len(word):
            return node.is_word

        for next_node in node.search(word[index]):
            if self._search(word, index + 1, next_node):
                return True

        return False
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, 0, self.root)


x = WordDictionary()


x.addWord("bad")
x.addWord("dad")
x.addWord("mad")
print(x.search("pad") == False)
print(x.search("bad") == True)
print(x.search(".ad") == True)
print(x.search("b..") == True)
