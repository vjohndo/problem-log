class SolutionHandlesSameNumAndOrdered(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quickSort(s, e):
            
            if e - s + 1 <= 1:
                return

            random_index = random.randint(s, e)
            nums[e], nums[random_index] = nums[random_index], nums[e]
            p = nums[e]
            slow = s
    
            for fast in range(s, e):
                if nums[fast] < p:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
                elif nums[fast] == p and random.random() >= 0.5:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1

            nums[slow], nums[e] = nums[e], nums[slow]

            quickSort(s, slow-1)
            quickSort(slow + 1, e)
        
        quickSort(0, len(nums) - 1)

        return nums

class SolutionQuickSortWhileLoopLeftRightPointer(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quickSort(s, e):
            
            if e - s + 1 <= 1:
                return

            p = nums[e]
            l = s
            r = e

            while l < r:
                if nums[l] >= p:
                    r -= 1
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    l += 1
            
            nums[l], nums[e] = nums[e], nums[l]

            quickSort(s, l-1)
            quickSort(l + 1, e)
        
        quickSort(0, len(nums) - 1)

        return nums

class SolutionQuickSortForLoopSlowFastsPointer(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, s, e):
        
        if e - s + 1 <= 1:
            return nums

        random_int = random.randint(s, e)
        nums[random_int], nums[e] = nums[e], nums[random_int]

        pivot = nums[e]
        left = s

        for i in range(s, e):
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        nums[e] = nums[left]
        nums[left] = pivot

        self.quickSort(nums, s, left - 1)
        self.quickSort(nums, left + 1, e)

        return nums