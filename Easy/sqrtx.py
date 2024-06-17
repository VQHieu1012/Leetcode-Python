class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right, ans = 0, x, 0

        while left <= right:
            mid = (left + right) // 2
            re = mid * mid

            if re == x:
                return mid
            elif re < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans