from typing import List 
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i,c in enumerate(s):
            last[ord(c)-ord('a')] = i
        ans = list()
        start = end = 0
        for i,c in enumerate(s):
            end = max(end,last[ord(c)-ord('a')])
            if i == end:
                ans.append(end - start + 1)
                start = end = i + 1
        return ans