from typing import List
class Solution:
    def searchMatrix0(self, matrix: List[List[int]], target: int) -> bool:
        self.ans = False
        n = len(matrix)
        m = len(matrix[0])
        def dfs(x,y):
            if matrix[x][y] == target:
                self.ans = True
            if x+1 < n and matrix[x+1][y] <= target:
                dfs(x+1,y)
            if y+1 < m and matrix[x][y+1] <= target:
                dfs(x,y+1)
        dfs(0,0)
        return self.ans
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        x, y = 0, m - 1
        while y >= 0 and x < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
        return False
if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    solution = Solution()
    print(solution.searchMatrix(matrix,target))