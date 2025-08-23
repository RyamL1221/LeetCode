# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 0ms (100.00%); Memory: 19.86MB (29.24%)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
        return valid(root, float("-inf"), float("inf"))
