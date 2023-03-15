class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def explore(grid, r, c):
            
            if (r, c) in visited or min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return 0
            
            visited.add((r, c))

            explore(grid, r + 1, c)
            explore(grid, r - 1, c)
            explore(grid, r, c + 1)
            explore(grid, r, c - 1)
            
            return 1
        
        count = 0
        for row in range(0,ROWS):
            for col in range(row % 2, COLS, 2):
                count += explore(grid, row, col)

        print(visited)

        return count