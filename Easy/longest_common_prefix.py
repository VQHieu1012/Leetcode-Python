class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        while len(strs) > 1:
            outStrs = []
            for i in range(0, len(strs), 2):
                s1 = strs[i]
                s2 = strs[i + 1] if i + 1 < len(strs) else strs[i]
                re = self.checkPre(s1, s2)
                print(re)
                outStrs.append(re)
            strs = outStrs
        return strs[0]

    def checkPre(self, s1, s2):      
        n = min(len(s1), len(s2))
        output = ''
        for i in range(n):
            if s1[i] != s2[i]:
                output += s1[i]   
            else:
                break   
        return output

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:

#         minstr, maxstr = min(strs), max(strs)

#         for i in range(len(minstr)):
#             if minstr[i] != maxstr[i]:
#                 return minstr[:i]
#         return minstr