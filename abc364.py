# n=int(input())
# s= [input() for _ in range((n))]
# flag=0
# for i in range(1,n):
#     if i != n-1 and s[i-1] == "sweet" and s[i] == "sweet":
#         print("No")
#         flag=1
#         break

# if flag == 0:
#     print("Yes")


# def move(H, W, grid, start_i, start_j, X):
#     current_i, current_j = start_i - 1, start_j - 1 
    
#     directions = {
#         'L': (0, -1),
#         'R': (0, 1),
#         'U': (-1, 0),
#         'D': (1, 0)
#     }
    
#     for move in X:
#         di, dj = directions[move]
#         new_i, new_j = current_i + di, current_j + dj
        
#         if 0 <= new_i < H and 0 <= new_j < W and grid[new_i][new_j] == '.':
#             current_i, current_j = new_i, new_j
    
#     return current_i + 1, current_j + 1

# H, W = map(int, input().split())
# start_i, start_j = map(int, input().split())
# grid = [input().strip() for _ in range(H)]
# X = input().strip()

# final_i, final_j = move(H, W, grid, start_i, start_j, X)

# print(final_i, final_j)


# def greed(N, A, B, X, Y):
#     dishes_sweet = sorted(zip(A, B), key=lambda x: x[0],reverse=True)
#     dishes_salty = sorted(zip(A, B), key=lambda x: x[1],reverse=True)

#     sweet_sum = 0
#     salt_sum = 0
#     min_dishes_sweet = N
#     for i, (a, b) in enumerate(dishes_sweet):
#         sweet_sum += a
#         salt_sum += b
#         if sweet_sum > X or salt_sum > Y:
#             min_dishes_sweet = i + 1
#             break
    
#     sweet_sum = 0
#     salt_sum = 0
#     min_dishes_salty = N
#     for i, (a, b) in enumerate(dishes_salty):
#         sweet_sum += a
#         salt_sum += b
#         if sweet_sum > X or salt_sum > Y:
#             min_dishes_salty = i + 1
#             break
    
#     return min(min_dishes_sweet, min_dishes_salty)


# N,X,Y = map(int, input().split())
# A= list(map(int, input().split()))
# B=list( map(int, input().split()))
# print(greed(N, A, B, X, Y))


# n,q = map(int, input().split())
# a = list(map(int, input().split()))
# b=[0]*q
# k=[0]*q
# for i in range(q):
#     b[i],k[i] = map(int, input().split())

# import bisect

# def find_kth_distances(n, q, a, queries):
#     a.sort()
#     results = []

#     for b, k in queries:
#         pos = bisect.bisect_left(a, b)
        
#         candidates = []
        
#         for i in range(max(0, pos - k), min(n, pos + k)):
#             candidates.append(abs(a[i] - b))
        
#         candidates.sort()
#         results.append(candidates[k-1])
    
#     return results

# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# queries = [tuple(map(int, input().split())) for _ in range(q)]

# results = find_kth_distances(n, q, a, queries)

# for result in results:
#     print(result)

# import bisect

# def find_kth_distances(n, q, a, queries):
#     a.sort()
#     results = []

#     for b, k in queries:
#         pos = bisect.bisect_left(a, b)
        
#         left_distances = [abs(a[i] - b) for i in range(max(0, pos - k), pos)]
#         right_distances = [abs(a[i] - b) for i in range(pos, min(n, pos + k))]
        
#         left_distances.sort()
#         right_distances.sort()
        
#         # Merge the two sorted lists and find the k-th smallest element
#         i = j = 0
#         merged_distances = []
        
#         while i < len(left_distances) and j < len(right_distances):
#             if left_distances[i] < right_distances[j]:
#                 merged_distances.append(left_distances[i])
#                 i += 1
#             else:
#                 merged_distances.append(right_distances[j])
#                 j += 1
        
#         while i < len(left_distances):
#             merged_distances.append(left_distances[i])
#             i += 1
        
#         while j < len(right_distances):
#             merged_distances.append(right_distances[j])
#             j += 1
        
#         results.append(merged_distances[k-1])
    
#     return results

# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# queries = [tuple(map(int, input().split())) for _ in range(q)]

# results = find_kth_distances(n, q, a, queries)

# for result in results:
#     print(result)



# N,X,Y = map(int, input().split())
# A=[0]*q
# B=[0]*q
# for i in range(q):
#     A[i],B[i] = map(int, input().split())

# def max_dishes_to_eat(N, X, Y, A, B):
#     # DPテーブルの初期化
#     dp = [[[-1] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
#     dp[0][0][0] = 0
    
#     for i in range(N):
#         for j in range(X + 1):
#             for k in range(Y + 1):
#                 if dp[i][j][k] == -1:
#                     continue
#                 # 料理iを食べない場合
#                 dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
#                 # 料理iを食べる場合
#                 new_j = min(j + A[i], X)
#                 new_k = min(k + B[i], Y)
#                 dp[i + 1][new_j][new_k] = max(dp[i + 1][new_j][new_k], dp[i][j][k] + 1)
    
#     # dpテーブルから最大値を取得
#     max_dishes = 0
#     for j in range(X + 1):
#         for k in range(Y + 1):
#             max_dishes = max(max_dishes, dp[N][j][k])
    
#     return max_dishes

# # 入力処理
# N, X, Y = map(int, input().split())
# A = [0] * N
# B = [0] * N
# for i in range(N):
#     A[i], B[i] = map(int, input().split())

# # 関数呼び出し
# print(max_dishes_to_eat(N, X, Y, A, B))
def max_dishes_to_eat(N, X, Y, A, B):
    # DPテーブルの初期化
    dp1 = [[float('inf')] * (X + 1) for _ in range(N + 1)]
    dp2 = [[float('inf')] * (Y + 1) for _ in range(N + 1)]
    dp1[0][0] = 0
    dp2[0][0] = 0
    
    for i in range(N):
        for j in range(X + 1):
            if dp1[i][j] != float('inf'):
                # 料理iを食べない場合
                dp1[i + 1][j] = min(dp1[i + 1][j], dp1[i][j])
                # 料理iを食べる場合
                if j + A[i] <= X:
                    dp1[i + 1][j + A[i]] = min(dp1[i + 1][j + A[i]], dp1[i][j] + B[i])
        
        for k in range(Y + 1):
            if dp2[i][k] != float('inf'):
                # 料理iを食べない場合
                dp2[i + 1][k] = min(dp2[i + 1][k], dp2[i][k])
                # 料理iを食べる場合
                if k + B[i] <= Y:
                    dp2[i + 1][k + B[i]] = min(dp2[i + 1][k + B[i]], dp2[i][k] + A[i])
    
    # dpテーブルから最大値を取得
    max_dishes = 0
    for i in range(N + 1):
        for j in range(X + 1):
            if dp1[i][j] <= Y:
                max_dishes = max(max_dishes, i)
        for k in range(Y + 1):
            if dp2[i][k] <= X:
                max_dishes = max(max_dishes, i)
    
    return max_dishes

# 入力処理
N, X, Y = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

# 関数呼び出し
print(max_dishes_to_eat(N, X, Y, A, B))
