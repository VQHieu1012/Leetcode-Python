class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:    
        n = len(nums)
        result = []
        permutation = []
        u = [False] * n
        def solve(index):
            
            for i in range(n):
                if u[i] == False:
                    print(u[i])
                    permutation.append(nums[i])
                    print(permutation)
                    u[i] = True
                    if len(permutation) == n and permutation not in result:
                        result.append(permutation.copy())
                    else:
                        solve(index + 1)
                    u[i] = False
                    permutation.pop()                
        solve(0)
        return result