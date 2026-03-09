class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            r = n - 1
            target = -nums[i]
            for l in range(i+1,n):
                if l > i + 1 and nums[l] == nums[l-1]:
                    continue
                while l < r and nums[l] + nums[r] > target:
                    r -= 1
                if l >= r :
                    break
                if  nums[l] + nums[r] == target:
                    ans.append([-target,nums[l],nums[r]])
        return ans
if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,0]
    print(solution.threeSum(nums))