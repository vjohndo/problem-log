class SolutionSingleList(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [0 for _ in range(n)]
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]
        
        return dp[0]

class SolutionBottomUp(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        prev = [0 for _ in range(n)]

        for r in range(m - 1, -1, -1):
            current = [0 for _ in range(n)]
            current[n - 1] = 1

            for c in range(n - 2, -1, -1):
                current[c] = prev[c] + current[c + 1]
            
            prev = current

        print(prev[0])
        return prev[0]

class SolutionTopDownMemoisation(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        cache = {}

        def paths(r, c):
            if r >= m or c >= n:
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            if r == m - 1 and c == n - 1:
                return 1
            
            cache[(r, c)] = paths(r + 1, c) + paths(r, c + 1)

            return cache[(r, c)]

        return paths(0, 0)

class SolutionTopDownRecursion(object):
    def uniquePaths(self, m, n):
        """
        TOP DOWN APPROACH - PURE RECURSION
        :type m: int
        :type n: int
        :rtype: int
        """

        def paths(r, c):
            if r >= m or c >= n:
                return 0

            if r == m - 1 and c == n - 1:
                return 1
            
            return paths(r + 1, c) + paths(r, c + 1)

        return paths(0, 0)