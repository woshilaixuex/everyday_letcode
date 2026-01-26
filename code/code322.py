from typing import List
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0] * (amount + 1)
        for i in range(1,amount+1):
            minNum = sys.maxsize
            for _,coin in enumerate(coins):
                if i - coin >= 0:
                    minNum = min(minNum,arr[i-coin])
            arr[i] = minNum + 1
        if arr[amount] == sys.maxsize + 1:
            return -1
        return arr[amount]
if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(solution.coinChange(coins,amount))