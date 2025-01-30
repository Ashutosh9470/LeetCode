from collections import deque

class Solution:
    def magnificentSets(self, n, edges):
        def is_bipartite(node, c, component):
            color[node] = c
            component.append(node)
            for nbr in adj[node]:
                if color[nbr] == c:
                    return False 
                if color[nbr] == -1 and not is_bipartite(nbr, 1 - c, component):
                    return False
            return True

        # Helper function to compute max depth (groups) for a component
        def max_groups_in_component(component):
            max_depth = 0
            for start in component:
                depth = [-1] * n
                q = deque()
                q.append(start)
                depth[start] = 0
                while q:
                    node = q.popleft()
                    for nbr in adj[node]:
                        if depth[nbr] == -1:
                            depth[nbr] = depth[node] + 1
                            max_depth = max(max_depth, depth[nbr])
                            q.append(nbr)
            return max_depth + 1  # Depth to groups conversion

        # Initialize adjacency list and color array
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        color = [-1] * n  # Tracks bipartition colors (0/1)
        components = []

        # Check bipartiteness and collect components
        for i in range(n):
            if color[i] == -1:
                component = []
                if not is_bipartite(i, 0, component):
                    return -1  # Non-bipartite component
                components.append(component)

        # Calculate total groups
        total = 0
        for comp in components:
            total += max_groups_in_component(comp)

        return total