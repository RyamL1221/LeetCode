# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 3ms (4.82%), Memory: 12.56MB (31.58%)
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        root.left, root.right = right_inverted, left_inverted
        return root
