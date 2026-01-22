from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for index,height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                idx,h = stack.pop()
                ans = max(ans,h * (index - idx))
                start = idx
            stack.append((start,height))
        while stack:
            idx,h = stack.pop()
            ans = max(ans,h * (len(heights) - idx))
        return ans
if __name__ == "__main__":
    heights = [5,4,1,2]
    solution = Solution()
    ans = solution.largestRectangleArea(heights)
    print(ans)