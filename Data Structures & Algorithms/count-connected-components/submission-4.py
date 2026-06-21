class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(n)]

        for a, b in edges:
            matrix[a][b] = 1
            matrix[b][a] = 1

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
                for neighbor, edge in enumerate(matrix[node]):
                    if edge == 1 and colors[neighbor] == WHITE:
                        colors[neighbor] = GREY
                        stack.append(neighbor)
                        pushed = True
                        break
                if not pushed:
                    colors[node] = BLACK
                    stack.pop()
        
        return count