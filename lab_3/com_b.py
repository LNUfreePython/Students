#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#with repetitions
def a_n_k(n,k):
  if k >= n:
    return 'invalid' 
  return factorial(n)//(factorial(n-k))

#without repetitions
def _a_n_k(n,k):
  return n**k

#combination
def C(n,k):
  return factorial(n)//factorial(k)*factorial(n-k)

#combination without repetitions
def _C(n,k):
  return factorial(n + k -1)//factorial(k)*factorial(n-1)


def Gen_perm(A):

    f = open("permutations.txt", "w")
    for i in range(factorial(len(A))):
        print("look at permutations.txt,generating connections in lexical order.txt")         
        f.write(str(i+1) + ': ' + str(A) + "\n")   
        p = len(A)-1

        while (p > 0) and (A[p-1] > A[p]):        
            p=p-1
        A[p:] = reversed(A[p:]) 
        if p > 0: 
            q = p 
            while A[p-1] > A[q]:   
                q=q+1
        A[p-1],A[q]=A[q],A[p-1]

    f.close()
        
A = [1,2,3,4,5,6]
A.sort()


def GenComb(k,n):
    B = []
    for i in range(k):
        B.append(i)
    B.append(n)
    B.append(0)
    while True:
        print(B[0:k])
        f = open("generating connections in lexical order.txt", "a")
        for j in range(len(B)-1):
            f.write("combinations" + ":"  + str(B) + "\n" ) 
            if B[j]+1 == B[j+1]:
                B[j]=j
            else:
                break
        if j < k:
            B[j] += 1
        else:
            break
    f.close()












       




