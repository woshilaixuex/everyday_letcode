def finds1m(nums: list[int]) -> int:
    for i in range(len(nums)):
        index = abs(nums[i])
        if nums[index] < 0:
            return index
        nums[index] = -nums[index]