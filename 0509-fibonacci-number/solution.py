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