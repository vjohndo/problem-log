class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_set = set()

        for num in nums:
            if num not in my_set:
                my_set.add(num)

            if num in my_set:
                my_set.remove(num)
        
        return my_set[0]