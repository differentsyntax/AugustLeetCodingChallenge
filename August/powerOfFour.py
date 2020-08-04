class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        if (num < 0 or num == 0):
            return False
        
        elif (num == 4):
            return True
        
        elif (num < 4 and num%4 == 1):
            return True
        
        elif (num%4 != 0):
            return False
                
        else:
            print(num//4)
            return (self.isPowerOfFour(num//4) and True)