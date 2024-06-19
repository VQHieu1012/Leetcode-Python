class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            leftSorted = mergeSort(left)
            rightSorted = mergeSort(right)

            return merge(leftSorted, rightSorted)
        
        def merge(left, right):
            re =  []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    re.append(left[i])
                    i += 1
                else:
                    re.append(right[j])
                    j += 1
            re.extend(left[i:])
            re.extend(right[j:])
            return re
        nums = mergeSort(nums)
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

