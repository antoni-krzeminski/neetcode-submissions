# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            root = TreeNode(val)
            return root
        curr = root
        new = TreeNode(val)
        while curr:
            if val > curr.val:
                if not curr.right:
                    curr.right = new
                    return root
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = new
                    return root
                curr = curr.left
        

            