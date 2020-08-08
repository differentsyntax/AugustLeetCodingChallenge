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
        y = 0
        main = []
        
        outPut[(x,y)] = [root.val]
        
        self.helper(root, outPut, x, y)
        
        xMapy = {}
        left = []
            
        for key in outPut:
            if key[0] not in left:
                left.append(key[0])
            if key[0] in xMapy:
                xMapy[key[0]].append(key[1])
            else:
                xMapy[key[0]] = [key[1]]
            
            xMapy[key[0]].sort(reverse=True)
        
        left.sort()
        
        for l in left:
            temp = []
            for r in xMapy[l]:
                temp.extend(outPut[(l, r)])
            main.append(temp)
        
        return(main)
        
    def helper(self, node, outPut, x, y):
        
        if node.left:
            if (x-1, y-1) in outPut:
                outPut[(x-1, y-1)].append(node.left.val)
            else:
                outPut[(x-1, y-1)] = [node.left.val]
            self.helper(node.left, outPut, x-1, y-1)
    
        if node.right:
            if (x+1, y-1) in outPut:
                outPut[(x+1, y-1)].append(node.right.val)
            else:
                outPut[(x+1, y-1)] = [node.right.val]
            self.helper(node.right, outPut, x+1, y-1)
            
        if not (node.left or node.right):
            return outPut