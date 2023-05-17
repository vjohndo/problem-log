class SolutionOwnSolution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        res = 0
        left = 31

        while n > 0:
            bit = n & 1
            n >>= 1
            res |= (bit << left)
            left -= 1
        
        return res

class SolutionNCSolutions:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res