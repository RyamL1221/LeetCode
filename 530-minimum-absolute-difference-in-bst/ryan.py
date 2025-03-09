# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 7ms (67.94%), Memory: 16.77MB (20.93%)
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sorted_tree = []

        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            sorted_tree.append(node.val)
            in_order_traversal(node.right)
        
        in_order_traversal(root)

        min_diff = float("inf")
        for i in range(len(sorted_tree) - 1):
            min_diff = min(sorted_tree[i + 1] - sorted_tree[i], min_diff)
        
        return min_diff
