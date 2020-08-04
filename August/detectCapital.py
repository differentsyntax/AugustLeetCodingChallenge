class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        capital = []
        small = []
        
        for elem in word:
            if elem.isupper():
                capital.append(elem)
            else:
                small.append(elem)
                
        if len(capital) == 0:
            return True
        
        if len(capital) == 1 and word[0] == capital[0]:
            return True
        
        if len(small) == 0:
            return True