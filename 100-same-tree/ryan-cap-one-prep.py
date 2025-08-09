# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Runtime: O(n), 0ms (100.00%); Memory: O(h)??? 17.88MB (39.75%)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return result
