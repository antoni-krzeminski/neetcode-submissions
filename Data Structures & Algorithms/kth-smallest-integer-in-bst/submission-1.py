# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curr = 1
        ans = []
        def dfs(node, curr):
            nonlocal ans

            if node.left:
                dfs(node.left, curr)
            print(node.val)
            ans.append(node.val)
            if node.right:
                dfs(node.right, curr)
        dfs(root, curr)
        # print(ans)
        return ans[k - 1]
            

            