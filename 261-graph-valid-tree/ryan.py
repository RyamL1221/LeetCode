class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges_dict = {i:[] for i in range(n)}

        for edge1, edge2 in edges:
            edges_dict[edge1].append(edge2)
            edges_dict[edge2].append(edge1)
        
        print(edges_dict)
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for edge in edges_dict[node]:
                if edge == prev: continue
                if not dfs(edge, node): return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n 
