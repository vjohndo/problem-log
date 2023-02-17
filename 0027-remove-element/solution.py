class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            else: 
                left += 1
        
        return left