from typing import List
from math import floor
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        ceil 上取整
        floor 下取整
        """
        n = len(matrix)
        if n <= 0:
            return False
        m = len(matrix[0])
        left = 0
        right = m * n - 1
        while (left < right):
            mid = left + right >> 1
            x = floor(mid / m)
            y = mid % m
            if matrix[x][y] == target:
                return True
            if (matrix[x][y] > target):
                right = mid - 1
            else:
                left = mid + 1
        x = floor(left / m)
        y = left % m
        return matrix[x][y] == target
if __name__ == "__main__":
    list = [[1]]
    solution = Solution()
    ans = solution.searchMatrix(list,3)
    print(ans)