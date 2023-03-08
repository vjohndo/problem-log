class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while len(q) > 0:
            res.append(q[-1].val)
            for _ in range(len(q)):
                curr = q.popleft() 
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
        return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                if i == 0:
                    res.append(curr.val)
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        
        return res