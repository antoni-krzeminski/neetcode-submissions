# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        currmax = root.val
        def dfs(root, max):
            nonlocal res
            newmax = max
            if root.val >= max:
                newmax = root.val

                res += 1
            if root.left:
                #print(root.left.val, newmax, res)
                dfs(root.left, newmax)
            if root.right:
                #print(root.right.val, newmax, res)

                dfs(root.right, newmax)
        
        dfs(root, currmax)
        return res

