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

class SolutionBFS(object):
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
                numCourses -= 1
                
        while q:
            current = q.popleft()
            for subsequent in adjList[current]:
                numPrereqs[subsequent] -= 1
                if numPrereqs[subsequent] == 0:
                    q.append(subsequent)
                    numCourses -= 1
                
        return numCourses == 0