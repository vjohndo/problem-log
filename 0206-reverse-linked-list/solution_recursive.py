class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHelper(None, head)
    
    def reverseListHelper(self, prev_node, current_node):
        if current_node is None:
            return prev_node

        next_node = current_node.next
        current_node.next = prev_node
        return self.reverseListHelper(current_node, next_node)