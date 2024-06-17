class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            re = 2 ** mid
            if re == n:
                return True
            elif re < n:
                left = mid + 1
            else:
                right = mid - 1
        return False