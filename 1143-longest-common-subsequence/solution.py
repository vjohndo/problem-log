class SolutionMemoisation(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        O(M*N) subproblems with each one requiring O(N)
        :type text1: str
        :type text2: str
        :rtype: int
        """
        cache = [ [ None for _ in range(len(text2))] for _ in range(len(text1)) ]

        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if cache[i][j] is not None:
                return cache[i][j]
            
            option_1 = lcs(i + 1, j)
            
            target_index = text2.find(text1[i], j)
            option_2 = 0
            if target_index != -1:
                option_2 = 1 + lcs(i + 1, target_index + 1)

            cache[i][j] = max(option_1, option_2)

            return cache[i][j] 
        
        return lcs(0, 0)


class SolutionBasicMemoisation(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Iterate through every subsequence of first string.
        # This is like a binary tree so we'd need to either do recursion / iterative

        cache = [ [ None for _ in range(len(text2))] for _ in range(len(text1))]

        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if cache[i][j] is not None:
                return cache[i][j]
            
            option_1 = lcs(i + 1, j)
            
            k = j
            while k < len(text2) and text1[i] != text2[k]:
                k += 1
            
            # Need to include this to handle case where no char exists
            if k >= len(text2):
                cache[i][j] = option_1
                return cache[i][j]

            option_2 = 1 + lcs(i + 1, k + 1)

            cache[i][j] = max(option_1, option_2)

            return cache[i][j] 
        
        return lcs(0, 0)

class SolutionBruteForce(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Iterate through every subsequence of first string.
        # This is like a binary tree so we'd need to either do recursion / iterative

        subs = []
        path = []

        def getSubsequences(i):
            if i >= len(text1):
                if len(path) <= text2:
                    subs.append(''.join(path))
                return
            
            path.append(text1[i])
            getSubsequences(i + 1)
            path.pop()
            getSubsequences(i + 1)
        
        getSubsequences(0)

        print(subs)

        def is_a_subsequence(sub, text):
            i = 0
            j = 0
            while i < len(sub) and j < len(text):
                if sub[i] != text[j]:
                    j += 1
                elif sub[i] == text[j]:
                    i += 1
                    j += 1
            
            return i == len(sub)

        max_seen = 0
        for sub in subs:
            if is_a_subsequence(sub, text2):
                max_seen = max(len(sub), max_seen)
            
        return max_seen

class SolutionFailedAttemptRefactored(object):
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
            # string_b --> abcd
            char = string_b.pop() # e

            res = 0
            
            while len(copy_a) > 0:
                if copy_a.pop() != char: # e != # e
                    continue
                else:
                    res = 1 + findSubsequence(list(text1), list(string_b)) # 1 + fs(zd, abcd)
                    break

            res = max(res, findSubsequence(list(text1), list(string_b))) # 1 + fs(zdebabc, abcd)

            return res
        
   
        return findSubsequence(string_a, string_b)


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