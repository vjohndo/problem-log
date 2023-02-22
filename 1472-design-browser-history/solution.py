class BrowserHistoryDOUBLYLINKEDLIST:
    class Node: 
        def __init__(self, val = None, prev = None, next = None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, homepage: str):
        self.home = self.Node(homepage)
        self.tail = self.home

    def visit(self, url: str) -> None:
        new_url = self.Node(url, self.tail, None)
        self.tail.next = new_url
        self.tail = self.tail.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.tail is not self.home:
            self.tail = self.tail.prev
            steps -= 1
        return self.tail.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.tail.next is not None:
            self.tail = self.tail.next
            steps -= 1
        return self.tail.val

class BrowserHistorySINGLEARRAYNOLOOPS:
    def __init__(self, homepage: str):
        self._arr = [homepage]
        self._curr = 0
        self._size = 1
        self._cap = 0

    def visit(self, url: str) -> None:
        self._curr += 1
        self._cap = self._curr
        if self._curr == self._size:
            self._arr.append(url)
            self._size += 1
        else:
            self._arr[self._curr] = url
        
    def back(self, steps: int) -> str:
        self._curr -= steps
        if self._curr < 0:
            self._curr = 0
        return self._arr[self._curr]
        

    def forward(self, steps: int) -> str:
        self._curr += steps
        if self._curr > self._cap:
            self._curr = self._cap
        return self._arr[self._curr]

class BrowserHistorySINGLEARRAY:

    # 1x Array
    # 1x Tail Pointer 
    # 1x Max Size Variable

    # When tail pointer == max size will need to append & tail++
    # When tail pointer < max can just update array & tail++

    def __init__(self, homepage: str):
        self._arr = [homepage]
        self._curr = 0
        self._size = 1
        self._cap = 0

    def visit(self, url: str) -> None:
        self._curr += 1
        self._cap = self._curr
        if self._curr == self._size:
            self._arr.append(url)
            self._size += 1
        else:
            self._arr[self._curr] = url
        
    def back(self, steps: int) -> str:
        while steps > 0 and self._curr > 0:
            self._curr -= 1 
            steps -= 1

        return self._arr[self._curr]
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self._curr < self._cap:
            self._curr += 1 
            steps -= 1

        return self._arr[self._curr]

class BrowserHistoryOG:
    def __init__(self, homepage: str):
        self._prv_stack = [homepage]
        self._fwd_stack = []
        
    def visit(self, url: str) -> None:
        self._prv_stack.append(url)
        self._fwd_stack = []

    def back(self, steps: int) -> str:

        while steps > 0 and len(self._prv_stack) > 1:
            curr_url = self._prv_stack.pop()
            self._fwd_stack.append(curr_url)
            steps -= 1

        return self._prv_stack[-1]

    def forward(self, steps: int) -> str:

        while steps > 0 and len(self._fwd_stack) > 0:
            self._prv_stack.append(self._fwd_stack.pop())
            steps -= 1
        
        return self._prv_stack[-1]
        