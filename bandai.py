import math

a,b,c = map(float,input().split())
d,e,f = map(float,input().split())
n = float(input())

magnitude = math.sqrt(d**2 + e**2 + f**2)

unit_d = d / magnitude
unit_e = e / magnitude
unit_f = f / magnitude

g = a + unit_d * n
h = b + unit_e * n
i = c + unit_f * n

print(g, h, i)
