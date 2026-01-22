from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for index,temperature in enumerate(temperatures):
            if stack:
                while stack:
                    temp = stack.pop()
                    if temp[1] >= temperature:
                        stack.append(temp)
                        break
                    else:
                        ans[temp[0]] = index - temp[0]
            stack.append((index,temperature))
        return ans
if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    soultion = Solution()
    ans = soultion.dailyTemperatures(temperatures)
    print(ans)