class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []

        current = root

        while current or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

class SolutionIterativeHacky(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []

        stack.append(root)

        while len(stack) > 0:
            print(stack)
            current = stack.pop()
            if current is None:
                continue

            if type(current) == int:
                result.append(current)
                continue

            stack.append(current.right)
            stack.append(current.val)
            stack.append(current.left)
    
        return result

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder(root, result):
            if not root:
                return
            
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        inorder(root, result)
        return result

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder(root, result)
        return result


    def inorder(self, root, result):
        if not root:
            return
        
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)