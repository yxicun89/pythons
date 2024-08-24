import math

X = int(input())
P = 100
r = 0.01

n = math.ceil(math.log(X / P) / math.log(1 + r))
print(n)
