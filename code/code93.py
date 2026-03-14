from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        addressPar = []
        hashSet = set()
        n = len(s)
        if n <= 3:
            return []
        def check(snum:str) -> bool:
            if len(snum) == 0:
                return False
            if len(snum) > 1 and snum[0] == '0':
                return False
            if  int(snum) > 255:
                return False
            return True
        def splitAddress(start:int):
            if len(addressPar) == 4:
                for address in addressPar:
                    if not check(address):
                        return
                adr = ".".join(addressPar)
                if adr not in hashSet:
                    ans.append(adr)
                    hashSet.add(adr)
            if start >= n:
                return
            for i in range(start,n):
                if len(addressPar) <= 2:
                    addressPar.append(s[start:i+1])
                else:
                    addressPar.append(s[start:])
                splitAddress(i+1)
                addressPar.pop()
        for i in range(n):
            addressPar.append(s[:i+1])
            splitAddress(i+1)
            addressPar.pop()
        return ans
    def restoreIpAddresses_ans(self, s: str) -> List[str]:
        ans = []
        path = []
        n = len(s)
        def dfs(start):
            if len(path) == 4:
                if start == n:
                    ans.append(".".join(path))
                return 
            for i in range(start,n):
                temp = s[start:i+1]
                if len(temp) > 1 and temp[0] == '0':
                    return
                if int(temp) > 255:
                    return
                path.append(temp)
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans
if __name__ == "__main__":
    solution = Solution()
    s = "1111"
    ans = solution.restoreIpAddresses_ans(s)
    print(ans)