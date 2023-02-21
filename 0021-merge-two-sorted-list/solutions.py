class Solution:
    def mergeTwoListsRefactored(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next

    def mergeTwoListsIMPROVED(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        cx = list1
        cy = list2

        if (cx.val < cy.val):
            head = cx
            cx = cx.next
        else:
            head = cy
            cy = cy.next

        current = head

        while cx is not None and cy is not None:
            if cy.val > cx.val:
                current.next = cx
                cx = cx.next
            else:
                current.next = cy
                cy = cy.next
            
            current = current.next
        
        if cx is None:
            current.next = cy
        else:
            current.next = cx

        return head

    def mergeTwoListsOG(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current_x = list1
        current_y = list2
        head = list1

        if (list1 is None and list2 is None):
            return None
        elif (list1 is None):
            return list2
        elif (list2 is None):
            return list1

        if (list1.val > list2.val):
            current_x = list2
            current_y = list1
            head = list2

        while current_x != None or current_y != None:
            next_x = current_x.next
            
            if current_y is None:
                break          
            
            if current_x.next is None:
                current_x.next = current_y
                break      

            if current_y.val < next_x.val:
                next_y = current_y.next 
                current_y.next = current_x.next
                current_x.next = current_y
                current_x = current_y
                current_y = next_y
            else:
                current_x = next_x

        return head