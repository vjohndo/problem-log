class SolutionDFS(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited or r >= ROWS or c >= COLS or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            count = 1
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        max_size = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_size = max(max_size, dfs(r, c))
                
        return max_size