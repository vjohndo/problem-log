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