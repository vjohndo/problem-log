class MinStack:

    def __init__(self):
        self._main_stack = []
        self._min_stack = [] 

    def push(self, val: int) -> None:
        self._main_stack.append(val)

        if not self._min_stack or val < self._min_stack[-1]:
            self._min_stack.append(val)
        else: 
            self._min_stack.append(self._min_stack[-1])

    def pop(self) -> None:
        self._main_stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._main_stack[-1]
        
    def getMin(self) -> int:
        return self._min_stack[-1]