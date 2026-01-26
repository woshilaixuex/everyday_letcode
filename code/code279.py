import sys
class Solution:
    def numSquares(self, n: int) -> int:
        arr = [0] * (n + 1)
        for i in range(1,n+1):
            minNum = sys.maxsize
            j = 1
            while (j * j) <= i:
                minNum = min(minNum,arr[i - j*j])
                j += 1
            arr[i] = minNum + 1
        return arr[n]
if __name__ == "__main__":
    solution = Solution()
    n = 12 
    print(solution.numSquares(n))