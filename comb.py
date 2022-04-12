#factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))


#with repetitions
def a_n_k(n,k):
  if k >= n:
    return 'invalid' 
  return factorial(n)//(factorial(n-k))


print(a_n_k(5,3))


#without repetitions
def _a_n_k(n,k):
    if k >= n:
        return 'invalid'
    return n**k


print(_a_n_k(5,3))


#combination with repetitions
def C(n,k):
    if k >= n:
        return 'invalid'
    return factorial(n)//factorial(k)*factorial(n-k)


print(C(5,3))

#combination without repetitions
def _C(n,k):
    if k >= n:
        return 'invalid'
    return factorial(n + k -1)//factorial(k)*factorial(n-1)


print(_C(5,3))

       




