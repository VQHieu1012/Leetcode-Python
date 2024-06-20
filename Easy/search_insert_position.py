class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        l, r = 0, len(nums) - 1
        mid = 0
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        if target < nums[mid]:
            return mid
        else:
            return mid + 1