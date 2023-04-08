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
    
class SolutionMergeSort:
    def sortArray(self, nums: List[int]) -> List[int]:
        print([0, 1][1:1])
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, start, end):
        print(nums[start:end+1])
        if  end - start + 1 <= 1:
            return nums

        middle = start + (end - start) // 2
        self.mergeSort(nums, start, middle)
        self.mergeSort(nums, middle + 1, end)

        self.merge(nums, start, middle, end)

        return nums

    def merge(self, nums, start, middle, end):
        i = 0
        j = 0
        k = start

        left = nums[start:middle+1]
        right = nums[middle+1:end + 1]

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


class SolutionInsertionSort:
    def sortArray(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            j = i - 1

            while j >= 0 and nums[j + 1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                j -= 1

        return nums