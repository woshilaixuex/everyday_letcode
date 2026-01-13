from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
             [[False] * m] * n会把每一行都分配相同的引用，故而，操作一个数会导致整列都跟着变
             所以二维以上拷贝最好循环赋值：boolArr = [[False for _ in range(m)] for _ in range(n)]
        """
        self.ans = False
        cx = [0,0,-1,1]
        cy = [1,-1,0,0]
        n = len(board)
        m = len(board[0])
        boolArr = [[False for _ in range(m)] for _ in range(n)]
        def returnBack(index:int,x:int,y:int):
            if index == len(word) - 1:
                self.ans = True
                return
            boolArr[x][y] = True
            for i in range(4):
                dx = cx[i] + x
                dy = cy[i] + y
                if 0 <= dx <= n - 1 and 0 <= dy <= m - 1 and board[dx][dy] == word[index+1] and not boolArr[dx][dy]:
                    returnBack(index+1,dx,dy)
            boolArr[x][y] = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    boolArr = [[False for _ in range(m)] for _ in range(n)]
                    returnBack(0,i,j)
                    if self.ans:
                        return True
        return False
if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
        ]
    word = "ABCESEEEFS"
    solution = Solution()
    print(solution.exist(board,word))