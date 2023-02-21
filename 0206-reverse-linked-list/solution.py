# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: return
        
        current_node = head
        prev_node = None

        while current_node != None:
            temp_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp_node

        return prev_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        current_node = head
        prev_node = None
        next_node = None

        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        head = prev_node

        return head

    def reverseListPrevPrev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        current_node = head
        prev_node = None
        prev_prev_node = None

        while current_node != None or prev_node != None:
            if prev_node is None:
                prev_node = current_node
                current_node = current_node.next
                continue
            
            prev_node.next = prev_prev_node
            prev_prev_node = prev_node
            prev_node = current_node

            if current_node is not None:
                current_node = current_node.next

        return prev_prev_node
