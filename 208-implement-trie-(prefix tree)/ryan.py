# Runtime: 122ms (31.40%), Memory: 38.76MB (56.50%)
class Trie(object):

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False 

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True
            
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
