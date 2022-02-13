class Solution:
    def romanToInt(self,s:str)-> int :
        inventory = {'I': 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000}
        
        sum = 0
        flag = true
        i = 0
        while i<=len(s)-2:
        
            if inventory[s[i]] <inventory[s[i+1]]:
                sum = sum + (inventory[s[i+1]]-inventory[s[i]])
                flag = False
                i = i+1
            else:
                sum += inventory [s[i]]
            i+=1
        if i == len(s)-1:
            sum += inventory[s[i]]
            
        return sum    
