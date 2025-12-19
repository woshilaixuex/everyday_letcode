from typing import List,Iterator
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        多源广搜
        """
        n = len(grid)
        if n is 0:
            return 0
        m = len(grid[0])
        queue = deque()
        for i,rows in grid:
            for j,_ in rows:
                if grid[i][j] is 2:
                    queue.append((i,j,0))
        def neighbors(x:int,y:int) -> Iterator[tuple[int,int]]:
            for dx,dy in ((x,y+1),(x,y-1),(x-1,y),(x+1,y)):
                if 0 <= dx < n and 0 <= dy < m:
                    yield dx,dy
        d = 0
        while queue:
            x,y,d = queue.popleft()
            for dx,dy in neighbors(x,y):
                if grid[dx][dy] is 1:
                    grid[dx][dy] = 2
                    queue.append((dx,dy,d+1))
        if any(1 in rows for rows in grid):
            return -1
        return d