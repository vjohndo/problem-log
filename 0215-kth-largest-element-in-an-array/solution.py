class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Regular sort but using len(arr) - k as the target

        def quickSelect(nums: List[int], s: int, e: int, k: int):
            if e - s + 1 <= 1:
                return nums[e]

            rand_int = random.randint(s, e)
            nums[rand_int], nums[e] = nums[e], nums[rand_int]

            pivot = nums[e]
            left = s

            for i in range(s, e):
                if nums[i] < pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

            nums[left], nums[e] = nums[e], nums[left]

            if len(nums) - k > left:
                return quickSelect(nums, left + 1, e, k)
            elif len(nums) - k < left:
                return quickSelect(nums, s, left - 1, k)
            else:
                return nums[left]

        return quickSelect(nums, 0, len(nums) - 1, k)

class SolutionRefactoredQuickSelect(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickSort(nums, s, e, k):
            if e - s + 1 <= 1:
                return nums[s]
            
            random_int = random.randint(s, e)
            nums[random_int], nums[e] = nums[e], nums[random_int]

            left = s
            pivot = nums[e]

            for i in range(s, e):
                if nums[i] > pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                
            nums[e] = nums[left]
            nums[left] = pivot

            if k - 1 == left:
                return nums[left]
            elif k - 1 < left:
                return quickSort(nums, s, left - 1, k)
            else:
                return quickSort(nums, left + 1, e, k)

        return quickSort(nums, 0, len(nums)-1, k)


class SolutionModifiedPivot(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, 0, len(nums)-1, k)

    def quickSort(self, nums, s, e, k):
        if s == k - 1 and e == k - 1:
            return nums[s]
        
        random_int = random.randint(s, e)
        nums[random_int], nums[e] = nums[e], nums[random_int]

        left = s
        pivot = nums[e]

        for i in range(s, e):
            if nums[i] > pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            
        nums[e] = nums[left]
        nums[left] = pivot

        if k - 1 == left:
            return nums[left]
        elif k - 1 < left:
            return self.quickSort(nums, s, left - 1, k)
        else:
            return self.quickSort(nums, left + 1, e, k)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        copy = nums[:]
        # print(self.quickSort(copy, 0, len(copy) -1))
        return self.quickSort(copy, 0, len(copy)-1)[k - 1]

    def quickSort(self, nums, s, e):
        if e - s + 1 <= 1:
            return nums
        
        left = s
        pivot = nums[e]

        for i in range(s, e):
            if nums[i] > pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            
        nums[e] = nums[left]
        nums[left] = pivot

        self.quickSort(nums, s, left - 1)
        self.quickSort(nums, left + 1, e)

        return nums
