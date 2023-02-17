class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique_ptr = 0
        dupes_ptr = 0
        current_dupe_value = nums[0]

        while dupes_ptr < len(nums) :
            if nums[dupes_ptr] != current_dupe_value:
                current_dupe_value = nums[dupes_ptr]
                unique_ptr += 1
                nums[unique_ptr], nums[dupes_ptr] = nums[dupes_ptr], nums[unique_ptr]
            
            dupes_ptr += 1

        return unique_ptr + 1

    def secondIteration(self, nums: List[int]) -> int:
        unique_ptr = 0
        dupes_ptr = 0
        current_dupe_value = nums[0]

        while nums[dupes_ptr] == current_dupe_value:
            dupes_ptr += 1

        current_dupe_value = nums[dupes_ptr]

        while dupes_ptr < len(nums) :
            if nums[dupes_ptr] == current_dupe_value:
                pass
            else:
                unique_ptr += 1
                nums[unique_ptr], nums[dupes_ptr - 1] = nums[dupes_ptr - 1], nums[unique_ptr]
                current_dupe_value = nums[dupes_ptr]
            
            dupes_ptr += 1

        return unique_ptr + 1

    def firstIteration(self, nums: List[int]) -> int:
        count = 1
        values_seen = 1
        last_seen = nums[0]
        i = 1

        while i < len(nums) and values_seen < len(nums):
            if nums[i] == last_seen:
                j = i
                while j + 1 < len(nums):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
            else:
                last_seen = nums[i]
                count += 1
                i += 1

            values_seen += 1

        return count