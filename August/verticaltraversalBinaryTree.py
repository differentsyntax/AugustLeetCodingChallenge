# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        outPut = {}
        x = 0
        main = []
        
        outPut[x] = [root.val]
        
        self.helper(root, outPut, x, main)
        
        return(main)
        
    def helper(self, node, outPut, x, main):
        
        if not (node.left or node.right):
            return True
         
        if node.left:
            if x-1 in outPut:
                outPut[x-1].append(node.left.val)
            else:
                outPut[x-1] = [node.left.val]
            self.helper(node.left, outPut, x-1, main)
    
        if node.right:
            if x+1 in outPut:
                outPut[x+1].append(node.right.val)
            else:
                outPut[x+1] = [node.right.val]
            self.helper(node.right, outPut, x+1, main)
            
        toSort = []
            
        for key in outPut:
            toSort.append(key)

        toSort.sort()

        for x in toSort:
            main.append(outPut[x])