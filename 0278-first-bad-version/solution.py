class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        first_bad = right

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return first_bad

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return right