class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        totalNumbers = 0
        for i in nums:
            totalNumbers ^= i

        return totalNumbers 

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         s = set(nums)
#         return sum(s) * 2 - sum(nums)
        