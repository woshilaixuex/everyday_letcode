from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        ret = []
        n = len(s)
        t = [[True] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                t[i][j] = (s[i] == s[j]) and t[i+1][j-1]
        def dfs(index:int):
            if index == n:
                ret.append(ans[:])
            for j in range(index,n):
                if t[index][j]:
                    ans.append(s[index:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)
        return ret