class Solution:
    def isPalindrome(self,x:int) -> bool:
        if x<0:
            return False
        ten = 10
        org = x
        num = 0 
        while x >= 10:
            num = (num* ten) +x % 10 
            x// = 10
        num = (num * ten) +x

        return num == org    22222
