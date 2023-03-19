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