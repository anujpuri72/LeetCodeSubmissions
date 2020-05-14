class Trie:

    def __init__(self):
        self.arr1 = []
        """
        Initialize your data structure here.
        """

    def insert(self, word: str) -> None:
        # print(self)
        self.arr1.append(word)
        """
        Inserts a word into the trie.
        """

    def search(self, word: str) -> bool:
        # print(self)
        if word in self.arr1:
            return True
        return False
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        # print(self)
        for i in self.arr1:
            if (i.startswith(prefix) == True):
                return True
        return False
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
