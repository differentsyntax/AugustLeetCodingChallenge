class MyHashSet:

    def __init__(self):
        
        self.hashSet = []

    def add(self, key: int) -> None:
        
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        
        if key in self.hashSet:
            ind = self.hashSet.index(key)
            for i in range(ind, len(self.hashSet) - 1):
                self.hashSet[i] = self.hashSet[i+1]

            self.hashSet = self.hashSet[:-1]

    def contains(self, key: int) -> bool:
        
        if key in self.hashSet:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)