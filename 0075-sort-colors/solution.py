class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # colors = [0] * 3 # also works
        colors = {0: 0, 1: 0, 2: 0}

        for num in nums:
            colors[num] += 1

        k = 0
        for num in range(0, len(colors)):
            for _ in range(0, colors[num]):
                nums[k] = num
                k += 1
        
        return nums