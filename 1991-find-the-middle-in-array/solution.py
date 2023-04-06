class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        left_sum = nums[left]
        right_sum = nums[right]
        

        # needs to check the next value
        while left < right:
            if left_sum >= right_sum:
                right -= 1
                right_sum += nums[right]
            else:
                left += 1
                left_sum += nums[left]
        
        if left_sum == right_sum:
            return left
        
        return -1