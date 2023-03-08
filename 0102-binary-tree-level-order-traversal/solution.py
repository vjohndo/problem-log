class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)
        
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                current = q.popleft()
                level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            res.append(level)

        return res

class SolutionNoLevel:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)
        
        while len(q) > 0:
            current = q.popleft()
            res.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

        return [res]