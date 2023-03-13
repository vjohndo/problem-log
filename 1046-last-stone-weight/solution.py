class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_stones = [-stone for stone in stones]
        heapq.heapify(max_stones)

        while len(max_stones) > 1:
            big = heapq.heappop(max_stones)
            small = heapq.heappop(max_stones)

            if big < small: # Notice how big < small in negative world
                heapq.heappush(max_stones, big - small)

        if len(max_stones) == 1:
            return -max_stones[0]
        
        return 0

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_stones = [-stone for stone in stones]
        heapq.heapify(max_stones)

        while len(max_stones) > 1:
            stone_1 = -heapq.heappop(max_stones)
            stone_2 = -heapq.heappop(max_stones)

            if stone_1 > stone_2:
                heapq.heappush(max_stones, -(stone_1 - stone_2))

        if len(max_stones) == 1:
            return -heapq.heappop(max_stones)
        
        return 0