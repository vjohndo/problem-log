class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        distances = [ ((coord[0]**2 + coord[1]**2), coord) for coord in points ]
        heapq.heapify(distances)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        return res

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        distances = [ (math.sqrt(coord[0]**2 + coord[1]**2), coord) for coord in points ]
        heapq.heapify(distances)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        return res