class Solution {
    public boolean validTree(int n, int[][] edges) {
        HashMap<Integer,HashSet<Integer>> adjList = new HashMap<Integer,HashSet<Integer>>();
        HashSet<Integer> visited = new HashSet<Integer>();
        for (int i = 0; i < n; i++) {
            adjList.put(i,new HashSet<Integer>());
        }
        for (int i = 0; i < edges.length; i++) {
            adjList.get(edges[i][0]).add(edges[i][1]);
            adjList.get(edges[i][1]).add(edges[i][0]);
        }
        Queue<int[]> queue = new LinkedList<int[]>();
        queue.add(new int[]{0,-1});
        while (!queue.isEmpty()) {
            int[] node = queue.remove();
            visited.add(node[0]);
            for (int edge: adjList.get(node[0])) {
                if (edge == node[1])
                    continue;
                if (visited.contains(edge) || edge == node[0])
                    return false;
                queue.add(new int[]{edge, node[0]});
            }
        }
        return n == visited.size();
    }
}
