# a, b, c = map(int, input().split())
# if (b <= a < c) or (b > c and (a >= b or a < c)):
#     print("No")
# else:
#     print("Yes")

# x=input()
# x=x.rstrip('0')
# if x[-1] == ".":
#     x=x.rstrip('.')
# print(x)

# n,k=,map(int,input().split())
# r=list(map(int,input().split()))



# from itertools import product

# n, k = map(int, input().split())
# r = list(map(int, input().split()))

# possible_combinations = product(*[range(1, r[i] + 1) for i in range(n)])

# valid_combinations = [comb for comb in possible_combinations if sum(comb) % k == 0]

# valid_combinations.sort()

# for comb in valid_combinations:
#     print(*comb)



# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# cumulative_sum = [0] * (n + 1)
# for i in range(1, n + 1):
#     cumulative_sum[i] = cumulative_sum[i - 1] + a[i - 1]

# pair_count = 0

# for i in range(n):
#     for j in range(i + 1, n):
#         distance = cumulative_sum[j + 1] - cumulative_sum[i]
#         if distance % m == 0:
#             pair_count += 1
        
#         reverse_distance = cumulative_sum[i] + (cumulative_sum[n] - cumulative_sum[j])
#         if reverse_distance % m == 0:
#             pair_count += 1

# print(pair_count)

# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# cumulative_sum = [0] * (n + 1)
# for i in range(1, n + 1):
#     cumulative_sum[i] = cumulative_sum[i - 1] + a[i - 1]

# remainder_count = {}
# pair_count = 0

# for i in range(n + 1):
#     remainder = cumulative_sum[i] % m
    
#     if remainder in remainder_count:
#         pair_count += remainder_count[remainder]
    
#     if remainder in remainder_count:
#         remainder_count[remainder] += 1
#     else:
#         remainder_count[remainder] = 1

# print(pair_count)

# a,b,c=map(int,input().split())
# n=int(input())
# p=[0]*n
# x=[0]*n
# y=[0]*n
# z=[0]*n
# for i in range(n):
#     p[i],x[i],y[i],z[i]=map(int,input().split())

# ans=float('inf')
# for i in range(n):
#     if (x[i] >= a or x[i] >= b or x[i] >= c) and (y[i] >= b or y[i] >= c) and (z[i] >= c):
#         ans=min(ans,p[i])

# if ans == float('inf'):
#     print(-1)
# else:
#     print(ans)

a, b, c = map(int, input().split())
n = int(input())
p = [0] * n
x = [0] * n
y = [0] * n
z = [0] * n

for i in range(n):
    p[i], x[i], y[i], z[i] = map(int, input().split())

ans = float('inf')
for i in range(n):
    if x[i] >= a and x[i] + y[i] >= a + b and x[i] + y[i] + z[i] >= a + b + c:
        ans = min(ans, p[i])

if ans == float('inf'):
    print(-1)
else:
    print(ans)
