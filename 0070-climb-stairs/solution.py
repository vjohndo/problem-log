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