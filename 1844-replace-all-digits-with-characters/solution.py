class SolutionBetter(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        def shift(char, num):
            return chr(ord(char) + int(num))

        res = list(s)

        for i in range(len(s)):
            if i % 2 != 0:
                res[i] = shift(s[i - 1], s[i])

        return "".join(res)

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        def shift(char, num):
            return chr(ord(char) + int(num))

        res = []

        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            else:
                res.append(shift(s[i - 1], s[i]))

        return "".join(res)

