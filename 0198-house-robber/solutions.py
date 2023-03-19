class Solution(object):
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
