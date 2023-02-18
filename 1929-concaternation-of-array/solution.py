class Solution:
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        return nums + nums

    
    def getConcatenation2(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [None] * (2 * n)

        for i in range(0,n):
            result[i] = nums[i]
            result[i + n] = nums[i]

        return result

    def getConcatenation3(self, nums: List[int]) -> List[int]:
        return nums * 2