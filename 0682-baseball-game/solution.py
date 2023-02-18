class Solution:
    def calPoints(self, operations: List[str]) -> int:

        score = []

        for operation in operations: 
            if operation == "+":
                previous = score[-1]
                penultimate = score[-2]
                score.append(previous + penultimate)
            elif operation == "D":
                previous = score[-1]
                score.append(previous * 2)
            elif operation == "C":
                score.pop()
            else:
                score.append(int(operation))
        
        return sum(score)