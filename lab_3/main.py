from com_b import a_n_k,factorial,_a_n_k,_C,C

def main():
  n = int(input ('Введіть n: '))
  k = int(input ('Введіть k: '))
  printer('Factorial', factorial(n))

  if n > k:
    printer('Permutation', a_n_k(n,k))
    printer('Permutation repeated', _a_n_k(n,k))
    printer('Combination', C(n,k))
    printer('Combination repeated', _C(n,k))
  elif k > n:
    print("k should be lover than n")

def printer(text, value):
  print(text + ': '  + str(value) )

main() 