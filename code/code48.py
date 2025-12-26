from typing import List
class Solution:
    # function1
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        function1: 设当前位置为i,j,对应旋转后的位置是(j,n-i-1)
        """
        n = len(matrix)
        matrix_copy = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_copy[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_copy
    # function2
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        水平这折叠+对角折叠
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                temp = matrix[n-i-1][j]
                matrix[n-i-1][j] = matrix[i][j]
                matrix[i][j] = temp
        for i in range(n):
            for j in range(i):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
    # function3
    def rotate3(self, matrix: List[List[int]]) -> None:
        """
        直接同时映射
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


