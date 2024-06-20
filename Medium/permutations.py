class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        permutation = []
        def solve(index):
            for i in nums:
                if i not in permutation:
                    permutation.append(i)
                        
                    if index == n - 1:
                        result.append(permutation.copy())
                        print(permutation)
                    else:     
                        solve(index + 1)
                    permutation.pop()
        solve(0)
        return result
    