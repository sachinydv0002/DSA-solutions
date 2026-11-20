# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        stack = []
        def inorder(root):
            if root:
                inorder(root.left)
                stack.append(root.val)
                inorder(root.right)
        
        inorder(root)

        dummy = TreeNode(0)
        head = dummy
        while stack:
            val = stack.pop(0)
            head.right = TreeNode(val)
            head = head.right
            
        return dummy.right