def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bottom up approach
        def dp(n):
            if n <= 3:
                return n
            vals = [2, 3]

            for i in range(4, n + 1):
                temp = vals[1]
                vals[1] += vals[0]
                vals[0] = temp
            
            return vals[1]
        
        return dp(n)

class SolutionImprovedTextbookApproach(object):
    def climbStairs(self, n):
        def helper(n):
            if n <= 3:
                return [n-1,n]
            a, b = helper(n - 1)
            return [b, a + b]
        
        return helper(n)[1]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Topdown, memoisation, caching
        def dp(n, cache):
            if n <= 3:
                return n
            
            if n in cache:
                return cache[n]
            
            cache[n] = dp(n-1, cache) + dp(n-2, cache)
            return cache[n]
        
        return dp(n, {})

