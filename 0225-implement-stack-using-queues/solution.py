class MyStack:
    class MyQueue:
        class Node:
            def __init__(self,val=None, nxt=None):
                self.val = val
                self.next = nxt

        def __init__(self, num = None):
            self.head = self.Node()
            self.tail = self.head
            self.n = 0

        def enqueue(self, val):
            self.tail.next = self.Node(val, None)
            self.tail = self.tail.next
            self.n += 1

        def dequeue(self):
            if self.n <= 0:
                return 
            
            returned = self.head.next
            self.head.next = self.head.next.next
            self.n -= 1

            if returned is self.tail:
                self.tail = self.head

            return returned.val

        def peek(self):
            if self.n > 0:
                return self.head.next.val
        
        def size(self):
            return self.n

        def is_empty(self):
            return self.n == 0
        
    def __init__(self):
        self.q = self.MyQueue()
       
    def push(self, x: int) -> None:

        n = self.q.size()
        self.q.enqueue(x)
        while n > 0:
            self.q.enqueue(self.q.dequeue())
            n -= 1

    def pop(self) -> int:
        if not self.q.is_empty():
            return self.q.dequeue()

    def top(self) -> int:
        if not self.q.is_empty():
            return self.q.peek()

    def empty(self) -> bool:
        return self.q.is_empty()

class MyStackRefactored:
    class MyQueue:
        class Node:
            def __init__(self,val=None, nxt=None):
                self.val = val
                self.next = nxt

        def __init__(self, num = None):
            self.head = self.Node()
            self.tail = self.head
            self.size = 0

        def enqueue(self, val):
            self.tail.next = self.Node(val, None)
            self.tail = self.tail.next
            self.size += 1

        def dequeue(self):
            if self.size <= 0:
                return 
            
            returned = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1

            if returned is self.tail:
                self.tail = self.head

            return returned.val

        def peek(self):
            if self.size > 0:
                return self.head.next.val
        
        def is_empty(self):
            return self.size == 0
        
    def __init__(self):
        self.q1 = self.MyQueue()
        self.q2 = self.MyQueue()

    def push(self, x: int) -> None:
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1.enqueue(x)
        
        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())

    def pop(self) -> int:
        if not self.q1.is_empty():
            return self.q1.dequeue()

    def top(self) -> int:
        if not self.q1.is_empty():
            return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()

class MyStack:
    class MyQueue:
        class Node:
            def __init__(self,val=None, nxt=None):
                self.val = val
                self.next = nxt

        def __init__(self, num = None):
            self.head = self.Node()
            self.tail = self.head
            self.size = 0


        def enqueue(self, val):
            self.tail.next = self.Node(val, None)
            self.tail = self.tail.next
            self.size += 1

        def dequeue(self):
            if self.size > 0:
                to_return = self.head.next

                if to_return is self.tail:
                    self.tail = self.head
                
                self.head.next = self.head.next.next

                self.size -= 1
                return to_return.val

        def peek(self):
            if self.size > 0:
                return self.head.next.val
        
        def get_size(self):
            return self.size
        
        def is_empty(self):
            return self.size <= 0
        
        def print(self):
            current = self.head
            while current is not None:
                print(current.val)
                if current is self.tail:
                    print("reached the tail")
                current = current.next
                

    def __init__(self):
        self.q1 = self.MyQueue("Q1")
        self.q2 = self.MyQueue("Q2")

    def push(self, x: int) -> None:
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1.enqueue(x)
        

        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())

    def pop(self) -> int:
        if not self.q1.is_empty():
            return self.q1.dequeue()

    def top(self) -> int:
        if not self.q1.is_empty():
            return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()