class Trie:
    words = {}
    sword = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}
        self.sword = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        lenw=len(word)
        i = 1
        while i <= lenw:
            self.sword[word[:i]] = 1
            i = i + 1
        self.words[word] = 1
        return 
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.words:
            return True
        return False 
    
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix in self.sword:
            return True
        return False 