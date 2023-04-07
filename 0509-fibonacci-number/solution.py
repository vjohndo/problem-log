class SolutionDP(object):
    def fib(self, n):
        if n <= 1:
            return n

        dp = [0, 1]

        i = 2
        while i <= n:
            temp = dp[1]
            dp[1] += dp[0]
            dp[0] = temp
            i += 1
        
        return dp[1]

class SolutionLinearRegression:
    def fib(self, n: int) -> int:
        return self.fib_helper(n)[0]

    def fib_helper(self, n):
        if n <= 1:
            return [n, 0]

        res_less1, res_less2 = self.fib_helper(n - 1)

        return [res_less1 + res_less2, res_less1]


class SolutionBinaryRegression:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)