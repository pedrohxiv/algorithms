def find_duplicate(nums):
    if len(nums) < 2:
        return False
    if any(not isinstance(num, int) or num < 0 for num in nums):
        return False
    nums.sort()
    for index in range(1, len(nums)):
        if (nums[index] == nums[index - 1]):
            return nums[index]
    return False
