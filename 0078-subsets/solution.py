class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        res.append([])

        def dfs(i, path):
            if i >= len(nums):
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                res.append(list(path))
                dfs(j + 1, path)
                path.pop()

        dfs(0, [])

        return res

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

class SolutionOGUnin:
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

class SolutionAddOnlyOnRightTraversal(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        res.append([])

        def dfs(i, path):
            if i >= len(nums):
                return
            
            path.append(nums[i])
            res.append(list(path))
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)
            

        dfs(0, [])

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