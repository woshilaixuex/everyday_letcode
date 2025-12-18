from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.roveX = [0,0,1,-1]
        self.roveY = [1,-1,0,0]
        def checkRotting() -> bool:
            for i in range(grid):
                for j in range(grid[0]):
                    if (grid[i][j] == 2):
                        return False
            return True
        if (checkRotting()):
            return 0
        
        return 0