class MyLinkedListREFACTORED:

    class Node:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail

        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        return self.findNodeAtIndex(index).val

    def addAtHead(self, val: int) -> None:
        self.spliceNewNode(val, self.head, self.head.next)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        self.spliceNewNode(val, self.tail.prev, self.tail)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        
        if index == self.length:
            return self.addAtTail(val)
        
        current = self.findNodeAtIndex(index)
        self.spliceNewNode(val, current.prev, current)
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        current = self.findNodeAtIndex(index)
        current.next.prev = current.prev
        current.prev.next = current.next
        self.length -= 1

    def spliceNewNode(self, val, prev, nxt):
        new_node = self.Node(val, prev, nxt)
        prev.next = new_node
        nxt.prev = new_node

    def findNodeAtIndex(self, index: int):
        current = self.head
        while index >= 0:
            current = current.next
            index -= 1

        return current

class MyLinkedListNOPREV:

    class Node:
        def __init__(self, val=None, next_node=None):
            self.val = val
            self.next = next_node

    def __init__(self):
        self.head = self.Node()
        self.tail = self.head
        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        return self.findNodeAtIndex(index).val

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val, self.head.next)
        self.head.next = newNode
        if self.head is self.tail:
            self.tail = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        self.tail.next = self.Node(val)
        self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        
        if index == self.length:
            return self.addAtTail(val)
        
        current = self.findNodeAtIndex(index - 1)
        current.next = self.Node(val, current.next)
        self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        current = self.findNodeAtIndex(index - 1)
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        self.length -= 1

    def findNodeAtIndex(self, index: int):
        current = self.head
        while index >= 0:
            current = current.next
            index -= 1
        return current
    

class MyLinkedListIMPROVED:

    class Node:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail

        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        current = self.head
        while index >= 0:
            current = current.next
            index -= 1
        
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        
        if index == self.length:
            return self.addAtTail(val)
        
        current = self.head
        while index >= 0:
            current = current.next
            index -= 1
        
        new_node = self.Node(val, current.prev, current)
        current.prev.next = new_node
        current.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        current = self.head
        while index >= 0:
            current = current.next
            index -= 1
        
        current.next.prev = current.prev
        current.prev.next = current.next
        self.length -= 1

class MyLinkedListOG:

    class Node:
        def __init__(self, value = None, next_node = None, prev_node = None):
            self.val = value
            self.prev = prev_node
            self.next = next_node

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.length = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        current_node = self.head

        while index >= 0:
            current_node = current_node.next
            index -= 1

        return current_node.val

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val, self.head.next, None)
        if new_node.next is self.tail:
            new_node.next = None
        self.head.next.prev = new_node
        self.head.next = new_node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val, None, self.tail.prev)
        if new_node.prev is self.head:
            new_node.prev = None
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.length:
            return

        if index == self.length:
            return self.addAtTail(val)

        if index == 0:
            return self.addAtHead(val)

        current_node = self.head

        while index >= 0:
            current_node = current_node.next
            index -= 1

        new_node = self.Node(val, current_node, current_node.prev)
        if new_node.next is self.tail:
            new_node.next = None
        if new_node.prev is self.head:
            new_node.prev = None

        current_node.prev.next = new_node
        current_node.prev = new_node

        self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:

        if index >= self.length:
            return
        
        current_node = self.head


        test_node = self.head
        while (test_node is not None):
            print(test_node.val)
            test_node = test_node.next

        while index >= 0:
            current_node = current_node.next
            index -= 1

        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head.next = current_node.next
        
        if current_node.next: 
            current_node.next.prev = current_node.prev
        else:
            self.tail.prev = current_node.prev
        
        self.length -= 1