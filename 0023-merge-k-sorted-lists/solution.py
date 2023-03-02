class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        prev_list = ListNode(None)

        for current_head in lists:
            result = ListNode(None)
            tail = result
            prev_head = prev_list.next

            while prev_head is not None and current_head is not None:
                if prev_head.val <= current_head.val:
                    tail.next = prev_head
                    tail = tail.next
                    prev_head = prev_head.next
                else:
                    tail.next = current_head
                    tail = tail.next
                    current_head = current_head.next

            if prev_head is None:
                tail.next = current_head
            else:
                tail.next = prev_head

            prev_list = result