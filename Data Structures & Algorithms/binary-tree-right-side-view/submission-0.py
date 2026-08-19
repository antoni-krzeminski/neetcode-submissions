# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = []
        stack.append(root)
        ans = []
        while stack:

            shortans = []
            newstack = []
            for q in stack:
                shortans.append(q.val)
                if q.left:
                    newstack.append(q.left)            
                if q.right:
                    newstack.append(q.right)            
            ans.append(shortans)

            stack = newstack
        return ans


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = self.levelOrder(root)
        answear = []
        for l in ans:
            answear.append(l[-1])
        return answear

        