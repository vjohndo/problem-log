class SolutionFullyPreprocessing(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        visited = set((0,0))
        q = collections.deque((0,0))
        directions = [[1,-1], [1,0], [1,1], [0,-1], [0,1], [-1,-1], [-1,0], [-1,1]]
        
        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return length

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if ((new_r, new_c) in visited or 
                            min(new_r, new_c) < 0 or 
                            max(new_r, new_c) >= n or  
                            grid[new_r][new_c] == 1):
                        continue
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))

            length += 1
        
        return -1
    
class SolutionPartialPreProcessing(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set((0,0))
        q = collections.deque([(0,0)])
        n = len(grid)
        directions = [[1,-1], [1,0], [1,1], [0,-1], [0,1], [-1,-1], [-1,0], [-1,1]]

        length = 1
        while len(q) > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                if min(r, c) < 0 or max(r, c) >= n or grid[r][c] == 1:
                    continue
                if r == n - 1 and c == n - 1:
                    return length
                for dr, dc in directions:
                    new_c = c + dc
                    new_r = r + dr
                    if (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

            length += 1

        return -1

class SolutionNoPreProcessing(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        visited = set()
        q = collections.deque()
        q.append((0,0))
        ROWS, COLS = len(grid), len(grid[0])

        length = 1
        while len(q) > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r, c) in visited or min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 1:
                    continue
                
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                visited.add((r,c))

                directions = [[1,-1], [1,0], [1,1], [0,-1], [0,1], [-1,-1], [-1,0], [-1,1]]
                for dr, dc in directions:
                    q.append((r + dr, c + dc))
            length += 1

        return -1