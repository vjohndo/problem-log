class SolutionWithSet(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        q = collections.deque()

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        mins = 0 
        # The 0ths miniutes represents the initial state
        # By adding an orrange to visited... you have declared it infected (which requires time to pass)
        while len(q) > 0:
            mins += 1
            for _ in range(len(q)):
                old_r, old_c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = old_r + dr, old_c + dc
                    if (min(r, c) < 0 or
                    r >= rows or
                    c >= cols or
                    (r, c) in visit or
                    grid[r][c] != 1):
                        continue
                    
                    visit.add((r, c))
                    q.append((r, c))
                    fresh -= 1
                    if fresh == 0:
                        return mins
        
        return -1
    
class SolutionNoSet(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        mins = 0
        while len(q) > 0:
            mins += 1
            for _ in range(len(q)):
                old_r, old_c = q.popleft()

                for dr, dc in directions:
                    r, c = old_r + dr, old_c + dc
                    if (min(r, c) < 0 or
                    r >= rows or
                    c >= cols or
                    grid[r][c] != 1):
                        continue
                    
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1
                    if fresh == 0:
                        return mins

        return -1