class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target: # Doesn't require to check the i value as we rely on the for loop to handle
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, path, total + candidates[j])
                path.pop()

        dfs(0, [], 0)

        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            path.append(candidates[i])
            dfs(i, path, total + candidates[i])
            
            path.pop()
            dfs(i + 1, path, total)

        dfs(0, [], 0)

        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            path.append(candidates[i])
            total += candidates[i]
            dfs(i, path, total)

            total -= candidates[i]
            path.pop()
            dfs(i + 1, path, total)

        dfs(0, [], 0)

        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if i >= len(candidates):
                return

            if sum(path) > target:
                return
            
            if sum(path) == target:
                res.append(path.copy())
                return
            
            path.append(candidates[i])
            dfs(i) # This is what makes it different to basic version of this eqn. You can call DFS on this level again.

            path.pop()
            dfs(i + 1)

        dfs(0)
        
        return res

class SolutionFailedAttempt:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            while i < len(candidates):
                path.append(i)

                if sum(path) > target:
                    path.pop()
                    return

                if sum(path) == target:
                    res.append(path.copy())
                    path.pop()
                    return
                
                for j in range(i, len(candidates)):
                    backtrack(i)
                
                path.pop()
                i += 1

        backtrack(0)

        return res