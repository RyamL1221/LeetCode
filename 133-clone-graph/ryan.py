"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Runtime: 42ms (66.36%); Memory: 18.3MB (39.87%)
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node) if node else None
