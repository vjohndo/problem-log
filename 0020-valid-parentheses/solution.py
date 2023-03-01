class SolutionRevision(object):
    def isValid(self, s):        
        matching_parentheses = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for char in s:
            if char not in matching_parentheses:
                stack.append(char)
                continue
            
            if len(stack) <= 0:
                return False

            if matching_parentheses[char] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) <= 0

class Solution:
    def isValidOG(self, s: str) -> bool:
        string_stack = []

        closing_brackets = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        
        for char in s:
            if char not in closing_brackets:
                string_stack.append(char)
            elif len(string_stack) < 1:
                return False 
            elif string_stack.pop() != closing_brackets[char]:
                return False

        return len(string_stack) == 0

    def isValidAlt(self, s: str) -> bool:
        string_stack = []

        closing_brackets = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        
        for char in s:
            if char not in closing_brackets:
                string_stack.append(char)
            elif not string_stack:
                return False 
            elif string_stack.pop() != closing_brackets[char]:
                return False

        return len(string_stack) == 0