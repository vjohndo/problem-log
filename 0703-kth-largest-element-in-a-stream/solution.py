class KthLargestUsingInBuiltClass(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]

class KthLargestHeapified(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums

        if nums:
            self.heap.append(self.heap[0])
        else:
            self.heap.append(None)

        i = (len(self.heap) - 1) // 2
        while i >= 1:
            self.downheap(i)
            # while i >= 1:
            #     j = i
            #     while j * 2 < len(self.heap):
            #         if (j * 2 + 1 < len(self.heap) and
            #         self.heap[j * 2 + 1] < self.heap[j * 2] and
            #         self.heap[j * 2 + 1] < self.heap[j]):
            #             self.heap[j * 2 + 1], self.heap[j] = self.heap[j], self.heap[j * 2 + 1]
            #             j = j * 2 + 1
            #         elif self.heap[j * 2] < self.heap[j]:
            #             self.heap[j * 2], self.heap[j] = self.heap[j], self.heap[j * 2]
            #             j = j * 2
            #         else:
            #             break
            #     i -= 1
            i -= 1
        
        while len(self.heap) - 1 > k:
            self.heap[1] = self.heap.pop()
            self.downheap(1)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """        
        if len(self.heap) - 1 < self.k:

            self.heap.append(val)
            i = len(self.heap) - 1
            self.upheap(i)

        elif val > self.heap[1]:
            self.heap[1] = val
            self.downheap(1)

        return self.heap[1]
    
    def upheap(self, j):
        if j > 1 and self.heap[j] < self.heap[j // 2]:
            self.heap[j], self.heap[j // 2] = self.heap[j // 2], self.heap[j]
            self.upheap(j // 2)
    
    def downheap(self, j):
        if j * 2 >= len(self.heap):
            return

        if j * 2 + 1 < len(self.heap) and self.heap[j * 2 + 1] < self.heap[j * 2] and self.heap[j * 2 + 1] < self.heap[j]:
            self.heap[j], self.heap[j * 2 + 1] = self.heap[j * 2 + 1], self.heap[j]
            self.downheap(j * 2 + 1)
        elif self.heap[j * 2] < self.heap[j]:
            self.heap[j], self.heap[j * 2] = self.heap[j * 2], self.heap[j]
            self.downheap(j * 2)

class KthLargestRecursive(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = [0]
        for num in nums:
            self.add(num)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """        
        if len(self.heap) - 1 < self.k:

            self.heap.append(val)
            i = len(self.heap) - 1
            self.upheap(i)

        elif val > self.heap[1]:
            self.heap[1] = val
            self.downheap(1)

        return self.heap[1]
    
    def upheap(self, j):
        if j > 1 and self.heap[j] < self.heap[j // 2]:
            self.heap[j], self.heap[j // 2] = self.heap[j // 2], self.heap[j]
            self.upheap(j // 2)
    
    def downheap(self, j):
        if j * 2 >= len(self.heap):
            return

        if j * 2 + 1 < len(self.heap) and self.heap[j * 2 + 1] < self.heap[j * 2] and self.heap[j * 2 + 1] < self.heap[j]:
            self.heap[j], self.heap[j * 2 + 1] = self.heap[j * 2 + 1], self.heap[j]
            self.downheap(j * 2 + 1)
        elif self.heap[j * 2] < self.heap[j]:
            self.heap[j], self.heap[j * 2] = self.heap[j * 2], self.heap[j]
            self.downheap(j * 2)

class KthLargestIterative(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = [0]
        for num in nums:
            self.add(num)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """        
        if len(self.heap) - 1 < self.k:
            # Regular push i.e. append and percolate up.
            self.heap.append(val)
            i = len(self.heap) - 1

            while i // 2 >= 1 and self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2

        elif val > self.heap[1]:
            # Only when a bigger minimum enters. 
            # Replace current minimum and percolate down. 
            self.heap[1] = val
            i = 1
            while i * 2 < len(self.heap):
                if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i] and self.heap[i * 2 + 1] < self.heap[i*2]:
                    self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
                elif self.heap[i * 2] < self.heap[i]:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i = i * 2
                else:
                    break
           
        return self.heap[1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)