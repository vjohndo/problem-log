class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res, stack = [], []
        current = root

        while stack or current:
            while current:
                res.append(current.val)
                stack.append(current)
                current = current.left

            current = stack.pop().right
        
        print(res)
        return res
