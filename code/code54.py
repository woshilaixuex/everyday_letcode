from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        bmatrix = [[False] * m for _ in range(n)]
        def check(zx,zy) -> bool:
            return zx >= 0 and zy >= 0 and zx < n and zy < m and not bmatrix[zx][zy]
        trans = [(0,1),(1,0),(0,-1),(-1,0)]
        step = 0
        x,y = 0,0
        for _ in range(n*m):
            ans.append(matrix[x][y])
            bmatrix[x][y] = True
            dx,dy = trans[step%4]
            zx,zy = x + dx,y + dy
            if check(zx,zy): 
                x,y = zx,zy
            else:
                step += 1
                dx,dy = trans[step%4]
                x,y = x + dx,y + dy
        return ans
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    ans = solution.spiralOrder(matrix)
    print(ans)
    