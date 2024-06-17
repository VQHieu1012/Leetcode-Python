class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        re = 0
        temp = x
        while x > 0:
            re = re * 10 + (x % 10)
            x = x // 10
        return re == temp