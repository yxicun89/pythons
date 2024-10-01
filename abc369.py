# a, b = map(int, input().split())

# count = 0

# # A と B の間の整数をカウント
# if abs(a-b) == 0:
#     count -= 1
# elif abs(a-b) % 2 == 0:
#     count += 1

# # A と B の外側の2つの整数をカウント
# count += 2

# print(count)


# N = int(input())
# A = []
# S = []

# for _ in range(N):
#     a, s = input().split()
#     A.append(int(a) - 1)  # 0-indexed に変換
#     S.append(s)

# # 初期化
# INF = float('inf')
# dp = [[[INF] * 100 for _ in range(100)] for _ in range(N + 1)]
# dp[0] = [[0] * 100 for _ in range(100)]  # 初期状態ではどの鍵盤に手を置いても疲労度は0

# # DPテーブルの更新
# for i in range(N):
#     for l in range(100):
#         for r in range(100):
#             if dp[i][l][r] == INF:
#                 continue
#             if S[i] == 'L':
#                 dp[i + 1][A[i]][r] = min(dp[i + 1][A[i]][r], dp[i][l][r] + abs(A[i] - l))
#             else:
#                 dp[i + 1][l][A[i]] = min(dp[i + 1][l][A[i]], dp[i][l][r] + abs(A[i] - r))

# # 最小疲労度を求める
# min_fatigue = INF
# for l in range(100):
#     for r in range(100):
#         min_fatigue = min(min_fatigue, dp[N][l][r])

# print(min_fatigue)


# def count_arithmetic_subarrays(A):
#     N = len(A)
#     count = 0
#     i = 0

#     while i < N:
#         j = i
#         while j + 1 < N and (j == i or A[j + 1] - A[j] == A[j] - A[j - 1]):
#             j += 1
#         length = j - i + 1
#         count += (length * (length - 1)) // 2
#         i = j + 1

#     return count + N

# # 指定された入力形式
# n = int(input())
# a = list(map(int, input().split()))

# # 等差数列の個数を求める
# result = count_arithmetic_subarrays(a)

# # 結果の出力
# print(result)

# def count_arithmetic_subarrays(A):
#     N = len(A)
#     count = 0

#     dp = [0] * N

#     for i in range(1, N):
#         if i > 1 and A[i] - A[i-1] == A[i-1] - A[i-2]:
#             dp[i] = dp[i-1] + 1
#         else:
#             dp[i] = 1

#         count += dp[i]

#     return count + N

# n = int(input())
# a = list(map(int, input().split()))

# print(count_arithmetic_subarrays(a))


# def max_experience(N, A):
#     dp = [0] * (N + 1)
    
#     for i in range(1, N + 1):
#         next_dp = dp[:]
#         for j in range(i):
#             if j % 2 == 0:
#                 next_dp[j + 1] = max(next_dp[j + 1], dp[j] + 2 * A[i - 1])
#             else:
#                 next_dp[j + 1] = max(next_dp[j + 1], dp[j] + A[i - 1])
#         dp = next_dp
#     return max(dp)

# N = int(input())
# A = list(map(int, input().split()))

# print(max_experience(N, A))


# def max_experience(N, A):
#     dp = [0] * (N + 1)
    
#     for i in range(1, N + 1):
#         for j in range(i, 0, -1):
#             if j % 2 == 0:
#                 dp[j] = max(dp[j], dp[j - 1] + 2 * A[i - 1])
#             else:
#                 dp[j] = max(dp[j], dp[j - 1] + A[i - 1])
    
#     return max(dp)

# N = int(input())
# A = list(map(int, input().split()))

# print(max_experience(N, A))

# def max_experience(N, A):
#     dp = [0] * (N + 1)
    
#     for i in range(1, N + 1):
#         value = A[i - 1]
#         for j in range(i, 0, -1):
#             if j % 2 == 0:
#                 dp[j] = max(dp[j], dp[j - 1] + 2 * value)
#             else:
#                 dp[j] = max(dp[j], dp[j - 1] + value)
    
#     return max(dp)

# N = int(input())
# A = list(map(int, input().split()))

# print(max_experience(N, A))


# def max_experience(N, A):
#     from functools import lru_cache

#     @lru_cache(None)
#     def dp(i, j):
#         if i == 0:
#             return 0
#         if j == 0:
#             return dp(i - 1, j)
#         if j % 2 == 0:
#             return max(dp(i - 1, j), dp(i - 1, j - 1) + 2 * A[i - 1])
#         else:
#             return max(dp(i - 1, j), dp(i - 1, j - 1) + A[i - 1])

#     return max(dp(N, j) for j in range(N + 1))

# N = int(input())
# A = list(map(int, input().split()))

# print(max_experience(N, A))


def max_experience(N, A):
    dp = [0] * (N + 1)
    
    for i in range(N):
        value = A[i]
        for j in range(i, -1, -1):
            if (i - j) % 2 == 0:
                dp[j + 1] = max(dp[j + 1], dp[j] + 2 * value)
            else:
                dp[j + 1] = max(dp[j + 1], dp[j] + value)
    
    return max(dp)

N = int(input())
A = list(map(int, input().split()))

print(max_experience(N, A))