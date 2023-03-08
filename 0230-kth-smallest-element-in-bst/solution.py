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