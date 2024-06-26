class Solution:
    def romanToInt(self, s: str) -> int:
        D = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        re = 0
        for i in range(len(s)):
            if i < len(s) - 1 and D[s[i]] < D[s[i + 1]]:
                re -= D[s[i]]
            else:
                re += D[s[i]]
        return re