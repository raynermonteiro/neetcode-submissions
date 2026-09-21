class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {1:1, 2:2}
        
        def f(x):
            if x in mem:
                return mem[x]
            else:
                mem[x] = f(x-1) + f(x-2)
                return mem[x]
        
        return f(n)