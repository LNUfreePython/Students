def searchInsert(self,n: List[int],target: int) -> int:
 i,j=0,len(n)-1
        while i<=j
            m = (i+j)//2
            if n[m]==target:
                return m
            elif n[m]>target:
                j=m-1
            else:
                i=m+1
        return i        Vasyl_8.py
