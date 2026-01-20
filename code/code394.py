class Solution:
    def decodeString(self, s: str) -> str:
        index = 0
        n = len(s)
        def getStr() -> str:
            nonlocal index
            ret = ""
            if index >= n or s[index] == ']':
                return ret
            if '0' <= s[index] <= '9':
                num = getDig()
                index += 1
                temp = getStr()
                index += 1
                while num > 0:
                    num -= 1
                    ret += temp
            else:
                ret += s[index]
                index += 1
            return ret + getStr()
        def getDig() -> int:
            nonlocal index
            num = 0
            while index < n and s[index].isdigit():
                num = num*10 + int(s[index])
                index += 1
            return num
        return getStr()
if __name__ == "__main__":
    solution = Solution()
    string = "3[a]2[bc]"
    print(solution.decodeString(string))