class SolutionFirstAttempt(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        alphabet_map = {}

        for i, char in enumerate(order):
            alphabet_map[char] = i

        def compare(a, b):
            i = 0

            while i < len(a) and i < len(b):
                if alphabet_map[a[i]] < alphabet_map[b[i]]:
                    return -1
                
                if alphabet_map[a[i]] > alphabet_map[b[i]]:
                    return 1

                i += 1
            
            if len(a) == len(b):
                return 0
            elif len(a) < len(b):
                return -1
            else:
                return 1

        for i in range(1, len(words)):
            if compare(words[i-1], words[i]) > 0:
                return False

        return True