# if
# 1 부등호
# A,B=input().split(" ")
# a = int(A)
# b = int(B)

# if a>b:
#   print(">")
# elif a<b:
#   print("<")
# else:
#   print("==")

# 2 시험 성적
# score=int(input())

# if score >= 90 and score<=100:
#   print("A")
# elif score >=80 and score<=89:
#   print("B")
# elif score >=70 and score<=79:
#   print("C")
# elif score >=60 and score<=69:
#   print("D")
# else:
#   print("F")

# 3 윤년 leap year
# year = int(input())
# if year%4==0:
#   if year%100!=0 or year%400==0:
#     print("1")
#   else:
#     print("0")
# else:
#   print("0")

# 4 사분면 고르기 Quadrant
# x = int(input())
# y = int(input())
# if x>0 and y>0:
#   print("1")
# elif x<0 and y>0:
#   print("2")
# elif x<0 and y<0:
#   print("3")
# elif x>0 and y<0:
#   print("4")

# 5 알람시계 문제 
# 시간 45분 앞당기기

H,M= input().split(" ")
h = int(H)
m = int(M)
if m>=45:
  m-=45
  print(h, m)
elif m <45 and h>0:
  h-=1
  m+=15
  print(h, m)
else:
  h = 23
  m+=15
  print(h, m)  