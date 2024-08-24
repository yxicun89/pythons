# R,G,B = map(int,input().split())
# C = input()

# if C == "Red":
#     print(min(G,B))
# elif C == "Green":
#     print(min(R,B))
# else:
#     print(min(R,G))

# import math

# xa,ya = map(int,input().split())
# xb,yb = map(int,input().split())
# xc,yc = map(int,input().split())

# ans = []
# ans.append(abs(xa-xb)**2 + abs(ya-yb)**2)
# ans.append(abs(xa-xc)**2 + abs(ya-yc)**2)
# ans.append(abs(xc-xb)**2 + abs(yc-yb)**2)

# ans.sort()
# if ans[2] == ans[1] + ans[0]:
#     print("Yes")
# else:
#     print("No")

# n=int(input())

# lr = [list(map(int,input().split())) for _ in range(n)]


# def find_sequence(n, lr):
#     dp = [{} for _ in range(n+1)]
#     dp[0][0] = [] 

#     for i in range(1, n+1):
#         Li, Ri = lr[i-1]
#         for s in dp[i-1]: 
#             for x in range(Li, Ri+1):  
#                 new_sum = s + x
#                 if new_sum not in dp[i]:
#                     dp[i][new_sum] = dp[i-1][s] + [x]

#     if 0 in dp[n]:
#         return dp[n][0]
#     else:
#         return None

# n = int(input())
# lr = [list(map(int, input().split())) for _ in range(n)]
# result = find_sequence(n, lr)

# if result:
#     print("Yes") 
#     print(*result)
# else:
#     print("No")


# def find_sequence(n, lr):
#     def dfs(index, current_sum, sequence):
#         if index == n:
#             if current_sum == 0:
#                 return sequence
#             else:
#                 return None
#         Li, Ri = lr[index]
#         for x in range(Li, Ri + 1):
#             result = dfs(index + 1, current_sum + x, sequence + [x])
#             if result is not None:
#                 return result
#         return None

#     result = dfs(0, 0, [])
#     return result

# n = int(input())
# lr = [list(map(int, input().split())) for _ in range(n)]
# result = find_sequence(n, lr)

# if result:
#     print("Yes")
#     print(*result)
# else:
#     print("No")

# def find_sequence(n, lr):
#     memo = {}

#     def dfs(index, current_sum):
#         if index == n:
#             return [] if current_sum == 0 else None
#         if (index, current_sum) in memo:
#             return memo[(index, current_sum)]

#         Li, Ri = lr[index]
#         for x in range(Li, Ri + 1):
#             result = dfs(index + 1, current_sum + x)
#             if result is not None:
#                 memo[(index, current_sum)] = [x] + result
#                 return memo[(index, current_sum)]

#         memo[(index, current_sum)] = None
#         return None

#     result = dfs(0, 0)
#     return result

# n = int(input())
# lr = [list(map(int, input().split())) for _ in range(n)]
# result = find_sequence(n, lr)

# import itertools

# def find_sequence(n, lr):

#     initial_sequence = []
#     initial_sum = 0
#     adjustments = []

#     for Li, Ri in lr:
#         mid = (Li + Ri) // 2
#         initial_sequence.append(mid)
#         initial_sum += mid
#         adjustments.append(range(Li - mid, Ri - mid + 1))

#     for comb in itertools.product(*adjustments):
#         adjusted_sum = initial_sum + sum(comb)
#         if adjusted_sum == 0:
#             return [initial_sequence[i] + comb[i] for i in range(n)]
    
#     return None

# n = int(input())
# lr = [list(map(int, input().split())) for _ in range(n)]
# result = find_sequence(n, lr)

# from itertools import product

# def find_sequence(n, lr):
#     mid = n // 2
#     left_part = lr[:mid]
#     right_part = lr[mid:]

#     def get_sums(ranges):
#         sums = {}
#         for comb in product(*[range(Li, Ri+1) for Li, Ri in ranges]):
#             total = sum(comb)
#             if total not in sums:
#                 sums[total] = comb
#         return sums

#     left_sums = get_sums(left_part)
#     right_sums = get_sums(right_part)

#     for left_sum, left_seq in left_sums.items():
#         if -left_sum in right_sums:
#             right_seq = right_sums[-left_sum]
#             return list(left_seq) + list(right_seq)

#     return None

# # 入力の受け取り
# n = int(input())
# lr = [list(map(int, input().split())) for _ in range(n)]
# result = find_sequence(n, lr)

def find_sequence(n, lr):
    offset = 10000 
    max_sum = 20000  
    dp = [None] * (2 * offset + 1)
    dp[offset] = []

    for i in range(n):
        Li, Ri = lr[i]
        next_dp = dp[:]
        for s in range(-offset, offset + 1):
            if dp[s + offset] is not None:
                for x in range(Li, Ri + 1):
                    new_sum = s + x
                    if new_sum == 0:
                        return dp[s + offset] + [x]
                    if next_dp[new_sum + offset] is None:
                        next_dp[new_sum + offset] = dp[s + offset] + [x]
        dp = next_dp

    return None

n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
result = find_sequence(n, lr)

if result:
    print("Yes")
    print(*result)
else:
    print("No")
