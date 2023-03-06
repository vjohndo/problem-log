class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsHelper(n)[0]

    def climbStairsHelper(self, n):
        if n <= 3: 
            return [n, 2] # Actually [n, n-1] is better. If n is > 3, it will just take [3, 2] and never need to go deeper. If n = 2, 1, 0. Only the first value will be accessed. Hence [n, n-1] is totally fine.
        a, b = self.climbStairsHelper(n - 1)
        return [a + b, a]

class SolutionFibonacciMethod:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsHelper(n)[0]

    def climbStairsHelper(self, n):
        if n <= 3: 
            return [n, max(n-1, 0)]
        a, b = self.climbStairsHelper(n - 1)
        return [a + b, a]

class SolutionRefactorred:
    def climbStairs(self, n: int) -> int:
        calculated = {}
        self.climbStairsHelper(n, calculated)
        return calculated[n]

    def climbStairsHelper(self, n, calculated):
        if n <= 3: 
            calculated[n] = n
            return n

        if calculated.get(n):
            return calculated[n]

        left = self.climbStairsHelper(n - 1, calculated)
        right = self.climbStairsHelper(n - 2, calculated)

        calculated[n] = left + right

        return calculated[n]

class SolutionMemoisationWithDictionary:
    def climbStairs(self, n: int) -> int:
        calculated = {}
        self.climbStairsHelper(n, calculated)
        print(calculated)
        return calculated[n]

    def climbStairsHelper(self, n, calculated):
        if n <= 3: 
            calculated[n] = n
            return n

        if calculated.get(n):
            return calculated[n]

        left = self.climbStairsHelper(n - 1, calculated)
        right = self.climbStairsHelper(n - 2, calculated)

        result = left + right
        calculated[n] = result

        return result

class SolutionMemoisationWithList:
    def climbStairs(self, n: int) -> int:
        calculated = [None] * (n + 1)
        self.climbStairsHelper(n, calculated)
        return calculated[n]

    def climbStairsHelper(self, n, calculated):
        if n <= 3: 
            calculated[n] = n
            return n

        if calculated[n]:
            return calculated[n]

        left = self.climbStairsHelper(n - 1, calculated)
        right = self.climbStairsHelper(n - 2, calculated)

        result = left + right

        calculated[n] = result

        return result

class SolutionBetterRecurrence:
    def climbStairs(self, n: int) -> int:
        if n <= 3: 
            return n

        return 2*self.climbStairs(n - 2) + self.climbStairs(n - 3)

class SolutionBruteForce:
    def climbStairs(self, n: int) -> int:
        if n <= 3: 
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n -2)