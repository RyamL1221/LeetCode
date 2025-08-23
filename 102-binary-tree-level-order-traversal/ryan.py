# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: 0ms (100.00%); Memory: 18.41MB (59.53%)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        result = []
        queue.append(root)

        while queue:
            level = []
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        
        return result
