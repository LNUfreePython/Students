from com_b import factorial
   
def Gen_perm(A): 
    for i in range(factorial(len(A))):          
        print((A))   
        p=len(A)-1
        while (p > 0) and (A[p-1] > A[p]):        
            p=p-1
        A[p:] = reversed(A[p:]) 
        if p > 0: 
            q = p 
            while A[p-1] > A[q]:   
                q=q+1
        A[p-1],A[q]=A[q],A[p-1]
    
A = [1,2,3,4,5,6]
A = list(A) 
A.sort() 
Gen_perm(A) 