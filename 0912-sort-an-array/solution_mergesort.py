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