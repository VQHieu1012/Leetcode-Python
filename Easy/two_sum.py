class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [None, None]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res[0] = i
                    res[1] = j
        return res
        