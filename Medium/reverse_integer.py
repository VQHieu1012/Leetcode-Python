class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            return -self.reverse(-int(x))
        
        num = 0
        while x > 0:
            digit = x % 10
            num = num * 10 + digit
            if num > (2**31 - 1) or num < (-2**31):
                return 0
            x = x // 10
        return num