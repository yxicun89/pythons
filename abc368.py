# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=a[n-k:]
# a=a[:n-k]
# print(*b+a)


# n=int(input())
# a=list(map(int,input().split()))
# count=0
# a.sort(reverse=True)

# while True:
#     a[0]-= 1
#     a[1]-= 1
#     a.sort(reverse=True)
#     count += 1
#     if a.count(0) == n-1 or a.count(0) == n:
#         break

# print(count)


# n=int(input())
# a=list(map(int,input().split()))

# t=0

# for i in range(n):
#     turns_to_next_3 = (3 - (t % 3)) % 3

#     # if a[i] >= (5-turns_to_next_3):
#     #     a[i] -= turns_to_next_3
#     #     t += turns_to_next_3
#     # else:
#     #     t += a[i]
#     #     a[i] = 0

#     if turns_to_next_3 == 0:
#         div = a[i]//5
#         mod = a[i]%5
#         t=t+div*3+mod
#     elif turns_to_next_3 == 1:
#         div = a[i]//5
#         mod = a[i]%5
#         t=t+div*3+mod
#     elif turns_to_next_3 == 2:
#         div = a[i]//5
#         mod = a[i]%5
#         t=t+div*3+mod

#     else:



# print(int(t))


# n = int(input())
# a = list(map(int, input().split()))

# t = 0

# for i in range(n):
#     div_3 = a[i] // 3 
#     t += div_3 * 2  
#     a[i] -= div_3 * 3  

#     if a[i] > 0:
#         t += a[i]
#         a[i] = 0

# print(t)


# n = int(input())
# a = list(map(int, input().split()))

# t = 0

# for i in range(n):
#     while a[i] > 0:
#         turns_to_next_3 = 3 - (t % 3) 

#         if a[i] >= turns_to_next_3:
#             a[i] -= turns_to_next_3
#             t += turns_to_next_3
#         else:
#             t += a[i]
#             a[i] = 0
#             break

#         remaining_turns = a[i] // 3
#         normal_turns = a[i] % 3

#         t += remaining_turns * 3 + normal_turns
#         a[i] -= remaining_turns * 3 + normal_turns

# print(t)





# from collections import defaultdict, deque

# def find_min_tree(N, K, A, B, V):
#     # グラフの隣接リスト表現を構築
#     graph = defaultdict(list)
#     for i in range(N - 1):
#         graph[A[i]].append(B[i])
#         graph[B[i]].append(A[i])

#     # K個の頂点からBFSを使って全ての頂点への最短距離を求める
#     distance = [-1] * (N + 1)
#     queue = deque()
    
#     # 指定された頂点をキューに追加し、距離を0に設定
#     for v in V:
#         queue.append(v)
#         distance[v] = 0
    
#     # BFSを実行
#     while queue:
#         current = queue.popleft()
#         for neighbor in graph[current]:
#             if distance[neighbor] == -1:
#                 distance[neighbor] = distance[current] + 1
#                 queue.append(neighbor)
    
#     # 最小の部分木を見つける
#     min_tree_size = 0
#     for i in range(1, N + 1):
#         if distance[i] != -1:
#             min_tree_size += 1
    
#     return min_tree_size

# # 入力
# n, k = map(int, input().split())
# a = [0] * (n - 1)
# b = [0] * (n - 1)
# for i in range(n - 1):
#     a[i], b[i] = map(int, input().split())
# v = list(map(int, input().split()))

# # 結果を出力
# print(find_min_tree(n, k, a, b, v))


# def minimum_T(n, a):
#     T = 0
#     for i in range(n):
#         while a[i] > 0:
#             T += 1
#             if T % 3 == 0:
#                 a[i] -= 3
#             else:
#                 a[i] -= 1
#     return T

# n = int(input())
# a = list(map(int, input().split()))

# print(minimum_T(n, a))




def minimum_T(n, a):
    T = 0

    for health in a:
        # 5で割った商と余りを計算
        quotient, remainder = divmod(health, 5)

        # セット数に基づいて必要なターン数を加算
        T += quotient * 3

        # 残りの余りに基づいて追加のターン数を加算
        if remainder > 0:
            if remainder <= 2:
                T += 1  # 余りが1または2なら1ターンで処理
            else:
                T += 2  # 余りが3以上なら2ターンで処理

    return T

# 入力処理
n = int(input())
a = list(map(int, input().split()))

# 結果を出力
print(minimum_T(n, a))
