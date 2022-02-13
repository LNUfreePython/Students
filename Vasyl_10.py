class Solution(object):
    def strStr(self,haystack,needle):
        n1, m1 = len(needle), len(haystack)
        if n1 == 0:
            return n1
        if m1 < n1:
            return -1
        for i in range(m1-n1 + 1):
            if haystack[i:i+n1] == needle:
                return i
        return -1        