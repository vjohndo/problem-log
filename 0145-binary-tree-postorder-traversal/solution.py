class SolutionMyIdealSolution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            temp = stack[-1]
            if temp.right:
                current = temp.right
            else:
                temp = stack.pop()
                res.append(temp.val)
                while stack and temp is stack[-1].right:
                    temp = stack.pop()
                    res.append(temp.val)
                
        return res

class SolutionAlternative:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            if stack[-1].right:
                current = stack[-1].right
            else:
                current = stack.pop()
                res.append(current.val)
                while stack and current is stack[-1].right:
                    current = stack.pop()
                    res.append(current.val)
                current = None

        return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        current = root

        while current or stack:
            while  current:
                stack.append(current)
                current = current.left

            temp = stack[-1].right
            if temp:
                current = temp
            else:
                temp = stack.pop()
                res.append(temp.val)
                while stack and temp is stack[-1].right:
                    temp = stack.pop()
                    res.append(temp.val)
                    
        return res

class SolutionIterativeMethod:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                stack.append(current)
                current = current.left

            current = stack.pop()
            if stack and stack[-1] is current:
                current = current.right
            else:
                res.append(current.val)
                current = None
            
        return res
