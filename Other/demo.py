class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        remember = 0
        D = {
            "0":{"0":[[0,0], [1,0]],
                 "1":[[1, 0], [0,1]]},
            "1":{"0":[[1,0], [0,1]],
                 "1":[[0,1], [1,1]]}
        }
        
        for i in range(max(m, n)):
            
            x, y = "0", "0"
            if i < m:
                x = a[m-i]
             
            if i < n:    
                y = b[n-i]
            