class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        if word not in self.words:
            self.words.append(word)
        
    def search(self, word: str) -> bool:
        length = len(word)
        ref = {}
        match = []
        count = 0
        nope = 0
        
        for ch in word:
            ref[count] = ch
            count += 1
            
        for el in self.words:
            nope = 0
            if len(el) == length:
                for x in range(0, len(el)):
                    if ref[x] != '.':
                        if ref[x] != el[x]:
                            nope = 1
                            
                if nope == 0:
                    return True
                
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)