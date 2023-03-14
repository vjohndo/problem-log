class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff_map = {}

        for index, num in enumerate(nums):
            if num in diff_map:
                return [diff_map[num], index]
            diff_map[target - num] = index