class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ordSet = set()
        n = len(s)
        r = 0
        ans = 0
        for i in range(n):
            if i != 0:
                ordSet.remove(s[i-1])
            while r < n and s[r] not in ordSet:
                ordSet.add(s[r])
                r = r + 1
            ans = max(ans,r - i)
        return ans
if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    ans = solution.lengthOfLongestSubstring(s)
    print(ans)