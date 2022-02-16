class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1, 1]
        for i in range(1, 45):
            fib.append(fib[i]+fib[i-1])
        return fib[n]