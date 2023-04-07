class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_node = root.right
                while min_node and min_node.left:
                    min_node = min_node.left
                
                root.val = min_node.val
                root.right = self.deleteNode(root.right, root.val)

        return root

class SolutionMaxOfLeftSubtree:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                max_left = self.findMaxNode(root.left)
                root.val = max_left.val
                root.left = self.deleteNode(root.left, max_left.val)
                
        return root


    def findMaxNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        while current is not None and current.right is not None:
            current = current.right
        return current

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                right_min_node = self.getMinNode(root.right)
                root.val = right_min_node.val
                root.right = self.deleteNode(root.right, right_min_node.val)
        
        return root
    
    def getMinNode(self, root):
        min_node = root
        while min_node and min_node.left:
            min_node = min_node.left
        return min_node