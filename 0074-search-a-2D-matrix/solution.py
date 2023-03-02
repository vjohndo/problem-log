class SolutionNoFunctions(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break

        if not top <= bot: # If the above while loop hasn't stopped due to exhasuted search
            return False

        row = matrix[(top + bot) // 2] # Remember that we actually want the mid value. Top and bot don't represent a single cell
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        
        return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def findRow(matrix, target):
            left = 0
            right = len(matrix) - 1

            while left <= right:
                mid = (left + right) // 2
                if matrix[mid][-1] < target:
                    left = mid + 1
                elif matrix[mid][0] > target:
                    right = mid - 1
                else:
                    return matrix[mid]

            return []

        def findCol(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return True
            
            return False

        potential_row = findRow(matrix, target)

        return findCol(potential_row, target)

