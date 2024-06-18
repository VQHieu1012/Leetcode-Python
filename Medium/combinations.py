class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def gen(index, path):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(index, n + 1):
                path.append(i)
                gen(i + 1, path)
                path.pop()
        gen(1, [])
        return result