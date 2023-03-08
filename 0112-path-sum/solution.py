class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        
        if not root.left and not root.right:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        
        if not root.left and not root.right:
            return targetSum == 0
        
        if self.hasPathSum(root.left, targetSum):
            return True
            
        if self.hasPathSum(root.right, targetSum):
            return True

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right and targetSum == 0:
            return True
        
        if self.hasPathSum(root.left, targetSum):
            return True

        if self.hasPathSum(root.right, targetSum):
            return True
        
        targetSum += root.val
        return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        total = 0

        def backtrack(root, targetSum):
            nonlocal total
            if root is None:
                return False

            total += root.val
            if not root.left and not root.right and total == targetSum:
                return True
            
            if backtrack(root.left, targetSum):
                return True

            if backtrack(root.right, targetSum):
                return True

            total -= root.val
            return False
            
        return backtrack(root, targetSum)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        total = 0

        def backtrack(root):
            nonlocal total
            if root is None:
                return False

            total += root.val
            if not root.left and not root.right and total == targetSum:
                return True
            
            if backtrack(root.left):
                return True

            if backtrack(root.right):
                return True

            total -= root.val
            return False
            
        return backtrack(root)