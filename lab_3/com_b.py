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
       




