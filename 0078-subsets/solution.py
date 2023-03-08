class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def findsubsets(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            findsubsets(i + 1)

            subset.pop()
            findsubsets(i + 1)

        findsubsets(0)
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        def findsubsets(i):
            res.append(path[:])
            while i < len(nums):
                path.append(nums[i])
                i += 1
                findsubsets(i)
                path.pop()
                
        findsubsets(0)
        return res

class SolutionAccepted:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        def findsubsets(i, path):
            res.append(path[:])
            while i < len(nums):
                path.append(nums[i])
                i += 1
                findsubsets(i, path)
                path.pop()
                
        findsubsets(0, path)
        return res