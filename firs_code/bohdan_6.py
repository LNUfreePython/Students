ef lengthOfLastWord1(self, s):
    res, s = 0, s.rstrip()
    while res < len(s) and s[-(res+1)].isalpha():
        res += 1
    return res
    
def lengthOfLastWord2(self, s):
    return len(s.split()[-1]) if s.split() else 0 
    
def lengthOfLastWord(self, s):
    return len(s.rstrip().split(' ')[-1])