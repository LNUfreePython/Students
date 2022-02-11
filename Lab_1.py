class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x/2
        result = 0
        while start < end:
            mid = (start + end)/2
            if mid*mid < x:
                 start = start +1
                 result = start
            else:
                end = mid +1
        return result       
                
            