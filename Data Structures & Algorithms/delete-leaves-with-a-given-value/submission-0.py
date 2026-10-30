# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, NoDefault0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        


        def traverse(node):
            if not node:
                return
            

            traverse(node.left)
            traverse(node.right)
            # czy lisc z lewej
            if node.left and node.left.val == target and not node.left.left and not node.left.right:
                node.left = None
            
            if node.right and node.right.val == target and not node.right.left and not node.right.right:
                node.right = None
            
        traverse(root)
        return root if root.val != target else None
