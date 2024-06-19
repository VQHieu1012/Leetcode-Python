class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        arr_sum = len(nums) * (len(nums) + 1) // 2
        return arr_sum - total
    