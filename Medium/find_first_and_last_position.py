class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        l, r = 0, len(nums) - 1
        mid = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                break
        if nums[mid] == target:
            l, r = mid, mid
            while l - 1 >= 0 and nums[l - 1] == target:
                l -= 1
            while r + 1 < len(nums) and nums[r + 1] == target:
                r += 1
            return [l, r]
        return [-1, -1]