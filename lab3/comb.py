def factorial(n): 
  if n == 1:
    return 1
  else:
    return (n * factorial(n-1))

def a_n_k(n,k):
  if k >= n:
    return 'invalid' 
  return factorial(n)//(factorial(n-k))


print(a_n_k(7,3))