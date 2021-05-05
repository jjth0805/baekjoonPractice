## for statement
def for_statement():
  ## 1 Times Table /九九
  # i = int(input())
  # for i in range(i,i+1):
  #   for j in range(1,10):
  #     print(f"{i} * {j} = {i*j}")

  ## 2 multiple (A+B)
  # T = int(input())
  # c = []
  # for i in range(T):
  #   A,B = input().split(" ")
  #   a = int(A)
  #   b = int(B)
  #   c.append(a+b)
  # for i in range(len(c)):
  #   print(c[i])

  ## 3 sum of 1~n　/たし算
  # n = int(input())
  # print(int(n*(n+1)/2))

  ## 4 Fast multiple (A+B)
  # import sys
  # T = int(input())
  # for i in range(T):
  #   A, B = map(int, sys.stdin.readline().split())
  #   print(A+B)

  ## 5 1~N print
  # import sys
  # N = int(sys.stdin.readline())
  # for i in range(1,N+1):
  #   print(i)

  ## 6 reverse 1~N print
  # import sys
  # N = int(sys.stdin.readline())
  # for i in reversed(range(1,N+1)):
  #   print(i)
  # for i in range(N,0,-1):
  #   print(i)

  ## 7 print Case#n
  # import sys
  # N = int(sys.stdin.readline())
  # c = []
  # for i in range(N):
  #   A, B = map(int, sys.stdin.readline().split())
  #   c.append(A+B)
  # for i in range(N):
  #   print(f"Case #{i+1}: {c[i]}")

  ## 8 print Case#n 2
  # import sys
  # N = int(sys.stdin.readline())
  # A = []
  # B = []
  # c = []
  # for i in range(N):
  #   a, b = input().split()
  #   A.append(int(a))
  #   B.append(int(b))
  #   c.append(A[i]+B[i])
  # for i in range(N):
  #   print(f"Case #{i+1}: {A[i]} + {B[i]} = {c[i]}")

  ## other ppl's solution
  ## T = int(input())
  ## for i in range(T):
  ##     A, B = map(int, input().split())
  ##     C = A+B
  ##     print("Case #%d: %d + %d = %d"%(i+1, A, B, C))

  ## 9 star *
  # import sys
  # N = int(sys.stdin.readline())
  # a=""
  # for i in range(1,N+1):
  #   a+="*"
  #   print(a)
  # for i in range(1, N+1):
  #   print("*"*i)

  ## 10 star * 2
  # import sys
  # N = int(sys.stdin.readline())
  # for i in range(1, N+1):
  #   print(" "*(N-i)+"*"*i)

  ## 11 for + if
  import sys
  N, X = map(int,sys.stdin.readline().split())
  A = list(map(int,sys.stdin.readline().split()))
  for i in range(N):
    if A[i]<X:
      print(A[i], end = " ")