class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        def dfs(curr,used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            prev = -11
            for j in range(len(nums)):
                if j in used or nums[j] == prev:
                    continue
                used.add(j)
                curr.append(nums[j])
                dfs(curr,used)
                used.remove(j)
                curr.pop()
                prev = nums[j]
        dfs([],set())
        return res

nums = [1, 1, 2]
s = Solution()
print(s.permuteUnique(nums))