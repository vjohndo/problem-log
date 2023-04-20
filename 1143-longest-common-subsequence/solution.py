class SolutionFailedAttempt(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        string_a = list(text1)
        string_b = list(text2)

        def findSubsequence(string_a, string_b):
            if len(string_a) == 0 or len(string_b) == 0:
                return 0
            
            copy_a = string_a # zd
            copy_b = string_b # abcd

            char = copy_b.pop() # e

            res = 0
            
            while len(copy_a) > 0:
                if copy_a.pop() != char: # e != # e
                    continue
                else:
                    res = 1 + findSubsequence(copy_a, copy_b)

            if len(string_b) > 0:
                string_b.pop()

            res = max(res, findSubsequence(string_a, string_b))

            return res
        
        if len(string_a) < len(string_b):
            return findSubsequence(string_b, string_a)
        else:
            return findSubsequence(string_a, string_b)