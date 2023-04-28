class SolutionSingleArray(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        m, n = len(text1), len(text2)
        res = [0 for _ in range(n)]
        dp = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                temp = 0
                if j + 1 < n:
                    temp = dp
                
                dp = res[j]
                
                if text1[i] == text2[j]:
                    res[j] = 1 + temp
                elif j + 1 < n:
                    res[j] = max(res[j], res[j + 1])

        return res[0]

class SolutionTwoArrayRecycled(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        m, n = len(text1), len(text2)
        prev = [0 for _ in range(n)]
        current = [0 for _ in range(n)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[j] = 1
                    if j + 1 < n:
                        current[j] += prev[j + 1]
                else:
                    current[j] = prev[j]
                    if j + 1 < n:
                        current[j] = max(current[j], current[j + 1]) 
            prev, current = current, prev
    
        return prev[0]

class SolutionTwoArrayRefactored(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        m, n = len(text1), len(text2)
        prev = [0 for _ in range(n)]

        for i in range(m - 1, -1, -1):
            current = [0 for _ in range(n)]
            
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[j] = 1
                    if j + 1 < n:
                        current[j] += prev[j + 1]
                else:
                    current[j] = prev[j]
                    if j + 1 < n:
                        current[j] = max(current[j], current[j + 1]) 
            prev = current
    
        return prev[0]

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        m, n = len(text1), len(text2) #5, #3

        prev = [0 for _ in range(n)] #[0, 0, 0]

        res = []

        for i in range(m - 1, -1, -1):
            current = [0 for _ in range(n)] #[0, 0, 1]
            
            for j in range(n - 1, -1, -1):
                # if m >= len(text1) or n >= len(text2):
                #     current[j] = 0

                # i = 4, j = 1
                
                if text1[i] == text2[j]: # e == c
                    current[j] = 1 #[0, 0, 1]
                    if j + 1 < n:
                        current[j] += prev[j + 1]
                else:
                    current[j] = prev[j] #[0, 0, 1]
                    if j + 1 < n:
                        current[j] = max(current[j], current[j + 1])  #[0, 1, 1]

            prev = current
            res.append(list(prev))
    
        for l in res[::-1]:
            print(l)

        return prev[0]

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        cache = [ [ None for _ in range(len(text2)) ] for _ in range(len(text1)) ]

        def lcs(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0
            
            if cache[p1][p2] is not None:
                return cache[p1][p2] 

            if text1[p1] == text2[p2]:
                cache[p1][p2] = 1 + lcs(p1 + 1, p2 + 1)
            else:
                cache[p1][p2] = max(lcs(p1 + 1, p2), lcs(p1, p2 + 1))
            
            return cache[p1][p2]
        
        return lcs(0, 0)
    
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