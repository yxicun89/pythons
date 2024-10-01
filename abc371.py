# Sab,Sac,Sbc = input().split()

# age_order = {'A': 0, 'B': 0, 'C': 0}

# if Sab == ">":
#     age_order['A'] += 1
# else:
#     age_order['B'] += 1

# if Sac == ">":
#     age_order['A'] += 1
# else:
#     age_order['C'] += 1

# if Sbc == ">":
#     age_order['B'] += 1
# else:
#     age_order['C'] += 1

# sorted_age_order = sorted(age_order.items(), key=lambda x: x[1])

# print(sorted_age_order[1][0])


# 初めて生まれた男の子の名前が太郎それ以外は太郎禁止

# n,m = map(int,input().split())
# dict = {}

# for i in range(m):
#     a,b = input().split()
#     a=int(a)
    
#     if b == 'M':
#         if a not in dict:
#             dict[a] = b
#             print("Yes")
#         else:
#             print("No")
#     else:
#         print("No")



# import itertools

# def min_cost_to_isomorphism(N, MG, edges_G, MH, edges_H, A):
#     # 隣接行列を作成
#     adj_G = [[0] * N for _ in range(N)]
#     adj_H = [[0] * N for _ in range(N)]
    
#     for u, v in edges_G:
#         adj_G[u-1][v-1] = 1
#         adj_G[v-1][u-1] = 1
    
#     for a, b in edges_H:
#         adj_H[a-1][b-1] = 1
#         adj_H[b-1][a-1] = 1
    
#     min_cost = float('inf')
    
#     # 頂点の順列を全て試す
#     for perm in itertools.permutations(range(N)):
#         cost = 0
#         for i in range(N):
#             for j in range(i+1, N):
#                 if adj_G[i][j] != adj_H[perm[i]][perm[j]]:
#                     cost += A[min(i, j)][max(i, j) - 1 - min(i, j)]
#         min_cost = min(min_cost, cost)
    
#     return min_cost

# # 入力の読み込み
# n = int(input())
# mg = int(input())
# u_v = [list(map(int, input().split())) for _ in range(mg)]
# mh = int(input())
# a_b = [list(map(int, input().split())) for _ in range(mh)]
# a = [list(map(int, input().split())) for _ in range(n-1)]

# # 最小コストを計算
# result = min_cost_to_isomorphism(n, mg, u_v, mh, a_b, a)
# print(result)



# import itertools

# def min_cost_to_isomorphism(N, MG, edges_G, MH, edges_H, A):
#     # 隣接行列を作成
#     adj_G = [[0] * N for _ in range(N)]
#     adj_H = [[0] * N for _ in range(N)]
    
#     for u, v in edges_G:
#         adj_G[u-1][v-1] = 1
#         adj_G[v-1][u-1] = 1
    
#     for a, b in edges_H:
#         adj_H[a-1][b-1] = 1
#         adj_H[b-1][a-1] = 1
    
#     min_cost = float('inf')
    
#     # 頂点の順列を全て試す
#     for perm in itertools.permutations(range(N)):
#         cost = 0
#         for i in range(N):
#             for j in range(i+1, N):
#                 if adj_G[i][j] != adj_H[perm[i]][perm[j]]:
#                     cost += A[min(i, j)][max(i, j) - 1 - min(i, j)]
#         min_cost = min(min_cost, cost)
    
#     return min_cost

# # 入力の読み込み
# n = int(input())
# mg = int(input())
# u_v = [list(map(int, input().split())) for _ in range(mg)]
# mh = int(input())
# a_b = [list(map(int, input().split())) for _ in range(mh)]
# a = [list(map(int, input().split())) for _ in range(n-1)]

# # 最小コストを計算
# result = min_cost_to_isomorphism(n, mg, u_v, mh, a_b, a)
# print(result)



# import itertools

# def min_cost_to_isomorphism(N, MG, edges_G, MH, edges_H, A):
#     # 隣接行列を作成
#     adj_G = [[0] * N for _ in range(N)]
#     adj_H = [[0] * N for _ in range(N)]
    
#     for u, v in edges_G:
#         adj_G[u-1][v-1] = 1
#         adj_G[v-1][u-1] = 1
    
#     for a, b in edges_H:
#         adj_H[a-1][b-1] = 1
#         adj_H[b-1][a-1] = 1
    
#     # DPテーブルの初期化
#     dp = [[float('inf')] * (1 << N) for _ in range(N)]
#     dp[0][0] = 0
    
#     # DPの更新
#     for mask in range(1 << N):
#         for i in range(N):
#             if dp[i][mask] == float('inf'):
#                 continue
#             for j in range(N):
#                 if mask & (1 << j):
#                     continue
#                 new_mask = mask | (1 << j)
#                 cost = 0
#                 for k in range(N):
#                     if mask & (1 << k):
#                         if adj_G[i][k] != adj_H[j][k]:
#                             cost += A[min(i, k)][max(i, k) - 1 - min(i, k)]
#                 dp[j][new_mask] = min(dp[j][new_mask], dp[i][mask] + cost)
    
#     # 最小コストを求める
#     min_cost = float('inf')
#     for i in range(N):
#         min_cost = min(min_cost, dp[i][(1 << N) - 1])
    
#     return min_cost

# # 入力の読み込み
# n = int(input())
# mg = int(input())
# u_v = [list(map(int, input().split())) for _ in range(mg)]
# mh = int(input())
# a_b = [list(map(int, input().split())) for _ in range(mh)]
# a = [list(map(int, input().split())) for _ in range(n-1)]

# # 最小コストを計算
# result = min_cost_to_isomorphism(n, mg, u_v, mh, a_b, a)
# print(result)


# import itertools

# def min_cost_to_isomorphism(N, MG, edges_G, MH, edges_H, A):
#     # 隣接行列を作成
#     adj_G = [[0] * N for _ in range(N)]
#     adj_H = [[0] * N for _ in range(N)]
    
#     for u, v in edges_G:
#         adj_G[u-1][v-1] = 1
#         adj_G[v-1][u-1] = 1
    
#     for a, b in edges_H:
#         adj_H[a-1][b-1] = 1
#         adj_H[b-1][a-1] = 1
    
#     # DPテーブルの初期化
#     dp = [[float('inf')] * (1 << N) for _ in range(N)]
#     dp[0][0] = 0
    
#     # DPの更新
#     for mask in range(1 << N):
#         for i in range(N):
#             if dp[i][mask] == float('inf'):
#                 continue
#             for j in range(N):
#                 if mask & (1 << j):
#                     continue
#                 new_mask = mask | (1 << j)
#                 cost = 0
#                 for k in range(N):
#                     if mask & (1 << k):
#                         if adj_G[i][k] != adj_H[j][k]:
#                             cost += A[min(i, k)][max(i, k) - min(i, k) - 1]
#                 dp[j][new_mask] = min(dp[j][new_mask], dp[i][mask] + cost)
    
#     # 最小コストを求める
#     min_cost = float('inf')
#     for i in range(N):
#         min_cost = min(min_cost, dp[i][(1 << N) - 1])
    
#     return min_cost

# # 入力の読み込み
# n = int(input())
# mg = int(input())
# u_v = [list(map(int, input().split())) for _ in range(mg)]
# mh = int(input())
# a_b = [list(map(int, input().split())) for _ in range(mh)]
# a = [list(map(int, input().split())) for _ in range(n-1)]

# # 最小コストを計算
# result = min_cost_to_isomorphism(n, mg, u_v, mh, a_b, a)
# print(result)




# n=int(input())
# x=list(map(int,input().split()))
# p=list(map(int,input().split()))
# Q=int(input())
# L_R = [list(map(int, input().split())) for _ in range(Q)]


import bisect

n = int(input())
x = list(map(int, input().split()))
p = list(map(int, input().split()))
Q = int(input())
L_R = [list(map(int, input().split())) for _ in range(Q)]

villages = list(zip(x, p))

def preprocess_villages(n, villages):
    sorted_villages = sorted(villages)
    X_sorted = [v[0] for v in sorted_villages]
    P_sorted = [v[1] for v in sorted_villages]
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + P_sorted[i]
    
    return X_sorted, prefix_sum

def query_population(L, R, X_sorted, prefix_sum):
    left = bisect.bisect_left(X_sorted, L)
    right = bisect.bisect_right(X_sorted, R) - 1
    
    if left > right:
        return 0
    
    return prefix_sum[right + 1] - prefix_sum[left]

X_sorted, prefix_sum = preprocess_villages(n, villages)

for L, R in L_R:
    result = query_population(L, R, X_sorted, prefix_sum)
    print(result)