class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        elements = {}
        output = []
        
        for num in nums:
            if num in elements:
                elements[num] += 1
                    
            else:
                elements[num] = 1
                
                
        for key in elements:
            if elements[key] == 2:
                output.append(key)
                
                
        return output