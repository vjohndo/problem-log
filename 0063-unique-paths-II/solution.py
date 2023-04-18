class SolutionRefactored(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0 for _ in range(cols)]
        prev[cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    prev[c] = 0
                elif c + 1 < cols:
                    prev[c] = prev[c] + prev[c + 1]
        
        return prev[0]

class SolutionSingleArray(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        prev = [0 for _ in range(cols)]

        if obstacleGrid[rows - 1][cols - 1] != 1:
            prev[cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            if obstacleGrid[r][cols - 1] == 1:
                prev[cols - 1] = 0

            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    prev[c] = 0
                else:
                    prev[c] = prev[c] + prev[c + 1]
        
        return prev[0]


class SolutionBottomUp(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        prev = [0 for _ in range(cols)]

        if obstacleGrid[rows - 1][cols - 1] != 1:
            prev[cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            current = [0 for _ in range(cols)]
            if obstacleGrid[r][cols - 1] != 1:
                current[cols - 1] = prev[cols - 1]

            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    current[c] = 0
                    continue
                    
                current[c] = prev[c] + current[c + 1]
            
            prev = current
        
        return prev[0]


class SolutionMemoisation(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = {}

        def path(r, c):
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]

            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[(r, c)] = path(r + 1, c) + path(r, c + 1)

            return cache[(r, c)]
        
        return path(0, 0)