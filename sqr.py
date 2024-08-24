import math

a,b,c=map(int,input().split())
if c - a - b < 0:
    print("No")
elif (c - a - b) ** 2 > 4 * a * b :
    print("Yes")
else:
    print("No")