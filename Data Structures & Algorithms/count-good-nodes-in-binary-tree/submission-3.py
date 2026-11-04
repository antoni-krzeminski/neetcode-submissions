# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr):
            nonlocal maxvalpath
            nonlocal ans
            old = maxvalpath
            if curr.val >= maxvalpath:
                maxvalpath = curr.val
                ans += 1
            
            if curr.left:
                dfs(curr.left)
            if curr.right:
                dfs(curr.right)
            maxvalpath = old
        ans = 0
        maxvalpath = -200
        dfs(root)
        return ans


