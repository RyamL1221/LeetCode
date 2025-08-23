# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 3ms (36.58%); Memory: 21.16MB (27.59%)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        def pre_order(node):
            if not node:
                return
            
            pre_order(node.left)
            arr.append(node.val)
            pre_order(node.right)
        
        pre_order(root)
        return arr[k - 1]
