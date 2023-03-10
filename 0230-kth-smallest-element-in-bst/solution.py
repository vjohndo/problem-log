class SolutionPython3GlobalVariables:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        seen = 0

        def dfs(root):
            nonlocal res
            nonlocal seen

            if root is None:
                return

            dfs(root.left)
            seen += 1
            if seen == k:
                res = root.val
            else:
                dfs(root.right)
        
        dfs(root)
        return res

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        current = root

        while current or root:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        current = root
        count = 0

        while current or root:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            current = current.right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root, res):
            if not root:
                return None

            if len(res) < k: 
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)

            return res
        
        return inorder(root, [])[k-1]

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        res = []

        def inorder(root):
            if not root:
                return root

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return res[k - 1]