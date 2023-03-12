class KthLargest(object):

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