class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(i.lower()  for i in s if i.isdigit() or i.isalpha())
        return a == a[::-1]