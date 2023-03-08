class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map = {}
        for index, value in enumerate(inorder):
            index_map[value] = index

        preorder_index = 0

        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            pivot = index_map[root_value]
            root.left = array_to_tree(left, pivot - 1)
            root.right = array_to_tree(pivot + 1, right)

            return root

        return array_to_tree(0, len(preorder) - 1) 

class SolutionNCApproach(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Base case == 0
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        
        mid = 0
        while preorder[0] != inorder[mid]:
            mid += 1

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) 
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

class SolutionFAILEDATTEMPT(object):
    def buildTreeHelper(preorder, inorder, s, e, head_index):
            if e - s + 1 <= 1:
                return TreeNode(preorder[e])
            
            root = TreeNode(preorder[head_index])

            left_left = s
            while preorder[s] != inorder[mid] and mid < e:
                left_left += 1


            root.left = buildTreeHelper(preorder, inorder, s + 1, mid - 1, s + 1)
            root.right = buildTreeHelper(preorder, inorder, mid + 1, e, mid + 1)

            return root

        return buildTreeHelper(preorder, inorder, 0, len(preorder) - 1, 0)