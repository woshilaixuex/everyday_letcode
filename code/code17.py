from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.nubMap = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        self.ans = []
        digitsLen = len(digits)
        def dfs(index:int,path:str):
            if (index >= digitsLen):
                self.ans.append(path)
                return
            number = digits[index]
            arr = self.nubMap[number]
            for n in arr:
                dfs(index+1,path+n)
        dfs(0,"")
        return self.ans
if __name__ == "__main__":
    digits = "7"
    solution = Solution()
    ans = solution.letterCombinations(digits)
    print(ans)