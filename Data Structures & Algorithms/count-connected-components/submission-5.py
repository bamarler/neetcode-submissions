class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        WHITE, GREY, BLACK = 0, 1, 2
        colors = [WHITE] * n
        count = 0

        for start in range(n):
            if colors[start] != WHITE:
                continue
            count += 1
            stack = [start]
            colors[start] = GREY
            while stack:
                node = stack[-1]
                pushed = False
                for neighbor in adj[node]:
                    if colors[neighbor] == WHITE:
                        colors[neighbor] = GREY
                        stack.append(neighbor)
                        pushed = True
                        break
                if not pushed:
                    colors[node] = BLACK
                    stack.pop()

        return count