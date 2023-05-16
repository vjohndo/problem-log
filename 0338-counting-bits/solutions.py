class SolutionNonDP(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = []
        i = 0

        def countBits(n):
            count = 0
            while n > 0:
                count += 1
                n &= n -1
            
            return count


        while i <= n:
            ans.append(countBits(i))
            i += 1
        
        return ans

class SolutionOffsetFromMostSignificantBitNC(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]
        
        return dp

class SolutionOffsetFromMostSignificantBitLC(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = [0] * (n + 1)
        current = 0
        offset = 1

        while offset <= n:
            while current < offset and current + offset <= n:
                ans[current + offset] = 1 + ans[current]
                current += 1
            
            current = 0
            offset <<= 1
        
        return ans

class SolutionBitShiftRight(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x >> 1] + (x & 1)

        return ans

class SolutionBitPopping(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        
        return ans