class SolutionFastestPossible(object):
    def countStudents(self, students, sandwiches):
        square_students = 0
        circle_students = 0
        for i in students:
            if i == 1:
                square_students += 1
            else:
                circle_students += 1

        for i in sandwiches:
            if i == 1:
                if square_students == 0:
                    break 
                square_students -= 1
            else:
                if circle_students == 0:
                    break 
                circle_students -= 1
        
        return circle_students + square_students

class SolutionProperModelling:
    def countStudents(self, students, sandwiches):

        q = collections.deque(students)

        for i in sandwiches:
            student = q[0] # Peek at the next student
            count = 0 # Number of students I've seen so far
            while student != i:
                if count >= len(q):
                    return len(q) # If I've seen every student, return the number of students
                q.append(q.popleft()) # Otherwise, move this student to back of line
                student = q[0] # Set the student to be the next in line so I can check if they're a match
                count += 1 # Increase the students I've seen
            q.popleft() # If I'm here satisfied.

        return 0

class SolutionNoDSARefactored:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)
        circle_student = students.count(0)
        square_student = n - circle_student

        i = 0
        while i < n:
            if sandwiches[i]:
                square_student -= 1
            else:   
                circle_student -= 1   

            # Optimisation would be to include the check inside each if statement rather than checking OR
            if square_student < 0 or circle_student < 0:
                return n - i
                
            i += 1

        return 0

class SolutionNoDSAImproved:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)
        circle_student = students.count(0)
        square_student = n - circle_student

        i = 0
        while i < n:
            if sandwiches[i]:
                square_student -= 1
                if square_student < 0:
                    return n - i
            else:   
                circle_student -= 1
                if circle_student < 0:
                    return n - i
                
            i += 1

        return 0

class SolutionNODATASTRUCTURES:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)
        
        circle_student = students.count(0)
        square_student = n - circle_student

        circle_sandwiches = sandwiches.count(0)
        square_sandwiches = n - circle_sandwiches

        if circle_student == circle_sandwiches:
            return 0
        elif circle_student < circle_sandwiches:
            i = 0
            while i < n and circle_student >= 0:
                if sandwiches[i] == 0:
                    circle_student -= 1
                i += 1 
            return n - i + 1
        else:
            i = 0
            while i < n and square_student >= 0:
                if sandwiches[i] == 1:
                    square_student -= 1
                i += 1
            return n - i + 1

class SolutionASINTENDED:

    class Node:
        def __init__(self, val = None, next = None):
            self.val = val
            self.next = next

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        left = self.Node()
        right = left

        for student in students:
            right.next = self.Node(student)
            right = right.next

        list.reverse(sandwiches)

        count = 0

        while len(sandwiches) > 0 and count < len(sandwiches):
            if left.next.val == sandwiches[-1]:
                sandwiches.pop()
                left.next = left.next.next
                count = 0
            else:
                right.next = left.next
                right = right.next
                left.next = left.next.next
                right.next = None
                count += 1
            
        return len(sandwiches)
