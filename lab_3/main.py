from com_b import a_n_k,factorial,_a_n_k,_C,C
#n = int(input ('Введіть n: '))
#k = int(input ('Введіть k: '))

#Factorial

#print (factorial(n))

#with repetitions

#print (a_n_k(n,k))

#without repetitions

#print (_a_n_k(n,k))

#combination with repetitions

#print (C(n,k))

#combinatio without repetitions

#print (_C(n,k))
n = int(input ('Введіть n: '))
k = int(input ('Введіть k: '))

def calc_funcs(a = a_n_k(n,k),b = _a_n_k(n,k),c = factorial(n),d = C(n,k),e = _C(n,k)):
    if n > k:
        print (a,b,c,d,e)
    elif k > n:
        print ("invalid")
calc_funcs()        
    


 
  

    


     
