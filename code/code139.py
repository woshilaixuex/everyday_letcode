from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        setMap = set()
        n = len(s)
        arr = [False] * (n+1)
        arr[0] = True
        for word in wordDict:
            setMap.add(word)
        for i in range(1,n+1):
            for j in range(0,i):
                if arr[j] == True:
                    arr[i] = arr[i] or s[j:i] in setMap
        return arr[n]
if __name__ == "__main__":
    solution = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(solution.wordBreak(s,wordDict))