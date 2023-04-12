class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        right = len(needle) - 1

        while right < len(haystack):
            j = 0
            k = left
            while j < len(needle):
                if needle[j] == haystack[k]:
                    j += 1
                    k += 1
                else:
                    break
            
            if k > right:
                return left

            left += 1
            right += 1
        
        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0
        while i <= len(haystack) - len(needle):
            j = i
            k = 0

            while k < len(needle):
                if haystack[j] != needle[k]:
                    break
                j += 1
                k += 1
            
            if k == len(needle):
                return i

            i += 1

        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for index in range(0, len(haystack) - len(needle) + 1):
            print(str(haystack[index:index + len(needle)]))
            if needle == str(haystack[index:index + len(needle)]):
                return index
        
        return -1