class SolutionDFS(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preMap = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            preMap[a].append(b)

        visit = set()

        def dfs(key):
            if key in visit:
                return False

            if len(preMap[key]) == 0:
                return True

            visit.add(key)

            for pre in preMap[key]:
                if not dfs(pre):
                    return False
            
            visit.remove(key)
            preMap[key] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

class SolutionRevisedBFS(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = {i : [] for i in range(numCourses)}
        dep = {i : 0 for i in range(numCourses)}

        for post, pre in prerequisites:
            adj[pre].append(post)
            dep[post] += 1

        q = collections.deque()

        for i in range(numCourses):
            if dep[i] == 0:
                q.append(i)

        while len(q) > 0:
            course = q.popleft()
            numCourses -= 1
            for nei in adj[course]:
                if dep[nei] == 0:
                    continue
                    
                if dep[nei] > 1:
                    dep[nei] -= 1
                    continue
                
                q.append(nei)
        
        return numCourses <= 0

class SolutionFailedToReadNumCoursesDuringRevision(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = {}
        dep = {}

        for post, pre in prerequisites:
            if post not in adj:
                adj[post] = []
                dep[post] = 0
            if pre not in adj:
                adj[pre] = []
                dep[pre] = 0
            
            adj[pre].append(post)
            dep[post] += 1


        completed = set()
        q = collections.deque()
        courses = 0

        for key, deps in dep.items():
            courses += 1
            if deps == 0:
                completed.add(key)
                q.append(key)

        while len(q) > 0:
            course = q.popleft()
            courses -= 1
            for nei in adj[course]:
                if nei in completed:
                    continue
                if dep[nei] > 1:
                    dep[nei] -= 1
                    continue
                
                completed.add(nei)
                q.append(nei)
        
        return courses <= 0

class SolutionBFSOG(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adjList = {}
        numPrereqs = {}
        q = collections.deque()

        for i in range(numCourses):
            adjList[i] = []
            numPrereqs[i] = 0

        for begin, end in prerequisites:
            adjList[begin].append(end)
            numPrereqs[end] += 1
        
        for i in range(numCourses):
            if numPrereqs[i] == 0:
                q.append(i)
                numCourses -= 1 # This one is reducing the courses as we add to queue (pre processing)
                
        while q:
            current = q.popleft()
            for subsequent in adjList[current]:
                numPrereqs[subsequent] -= 1 # Unecessary work.
                if numPrereqs[subsequent] == 0:
                    q.append(subsequent)
                    numCourses -= 1
                
        return numCourses == 0