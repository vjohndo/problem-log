class SolutionDP(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], max(nums[0], nums[1])]
        
        i = 2
        while i < len(nums):
            temp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = temp

            i += 1

        return dp[1]

class SolutioTopDownRefactored(object):    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}

        def dp(i):
            if i in cache:
                return cache[i]
            
            max_a = 0
            for j in range(i + 2, len(nums)):
                max_a = max(dfs(j), max_a)
            max_a += nums[i]

            max_b = 0
            for j in range(i + 1, len(nums)):
                max_b = max(dfs(j), max_b)
            
            cache[i] = max(max_a, max_b)
            return cache[i]

        return dp(0)

class SolutionTopDown(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def dp(i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            max_val = 0
            for j in range(i + 2, len(nums)):
                amount = dp(j, cache)
                if amount > max_val:
                    max_val = amount
            
            count_1 = nums[i] + max_val

            max_val = 0
            for j in range(i + 1, len(nums)):
                amount = dp(j, cache)
                if amount > max_val:
                    max_val = amount

            count_2 = max_val

            cache[i] = max(count_1, count_2)
            return cache[i]

        return dp(0, {})

class SolutionBinaryRecursiveApproach(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cache = {}
        path = []

        def dfs(i):
            if i >= len(nums):
                return sum(path)

            path.append(nums[i])
            max_a = dfs(i + 2)

            path.pop()
            max_b = dfs(i + 1)

            return max(max_a, max_b)
        
        return dfs(0)

class SolutionTreeRecursion(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cache = {}
        path = []

        def dfs(i):
            if i >= len(nums):
                return 0

            
            path.append(nums[i])
            max_a = sum(path)
            for j in range(i + 2, len(nums)):
                max_a = max(dfs(j), max_a)

            path.pop()
            max_b = sum(path)
            for j in range(i + 1, len(nums)):
                max_b = max(dfs(j), max_b)

            return max(max_a, max_b)
        

        return dfs(0)