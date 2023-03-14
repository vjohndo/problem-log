class SolutionRefactored(object):
    def minEatingSpeed(self, piles, h):

        def isEnoughTime(piles, h, k):
            total_visits = 0

            for bananas in piles:
                total_visits += - (bananas // -k)

            return total_visits <= h

        left = 1
        right = max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2
            if isEnoughTime(piles, h, mid):
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return k

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
    
        def isEnoughTime(piles, h, k):
            total_visits = 0

            for bananas in piles:
                total_visits += - (bananas // -k)

            if total_visits <= h:
                return True
            
            return False

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if isEnoughTime(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        
        return right

class SolutionAttempt1(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
    
        def isEnoughTime(piles, h, k):
            visits = [-(bananas// -k) for bananas in piles]
            total_visits = sum(visits)

            if total_visits <= h:
                return True
            
            return False

        # print(isEnoughTime([3,6,7,11], 8, 3))
        # print(isEnoughTime([3,6,7,11], 8, 4))
        # print(isEnoughTime([3,6,7,11], 8, 5))

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if isEnoughTime(piles, h, mid):
                left = mid # INCORRECT HERE ... should be right = mid
            else:
                right = mid - 1 # INCORRECT HERE ... should be left = mid + 1
        
        return left