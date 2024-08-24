# y=int(input())
# if y % 400 == 0:
#     print(366)
# elif y % 400 != 0 and y % 100 == 0:
#     print(365)
# elif y % 400 != 0 and y % 100 != 0 and y % 4 == 0:
#     print(366)
# elif y % 400 != 0 and y % 100 != 0 and y % 4 != 0:
#     print(365)


# from heapq import nlargest, nsmallest
# n=int(input())
# a=list(map(int,input().split()))

# result = [(value,i)for i,value in enumerate(a)]
# max_result = nlargest(n, result)

# print(max_result[1][1]+1)


# def binary(n, m, a):
#     def is_valid(x):
#         return sum(min(x, cost) for cost in a) <= m

#     left, right = 0, max(a)
    
#     while left <= right:
#         mid = (left + right) // 2
#         if is_valid(mid):
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     if right == max(a) and is_valid(right):
#         return "infinite"
    
#     return right

# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# print(binary(n, m, a))

# y=int(input())
# if y % 400 == 0:
#     print(366)
# elif y % 400 != 0 and y % 100 == 0:
#     print(365)
# elif y % 400 != 0 and y % 100 != 0 and y % 4 == 0:
#     print(366)
# elif y % 400 != 0 and y % 100 != 0 and y % 4 != 0:
#     print(365)


# from heapq import nlargest, nsmallest
# n=int(input())
# a=list(map(int,input().split()))

# result = [(value,i)for i,value in enumerate(a)]
# max_result = nlargest(n, result)

# print(max_result[1][1]+1)


# def binary(n, m, a):
#     def is_valid(x):
#         return sum(min(x, cost) for cost in a) <= m

#     left, right = 0, max(a)
    
#     while left <= right:
#         mid = (left + right) // 2
#         if is_valid(mid):
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     if right == max(a) and is_valid(right):
#         return "infinite"
    
#     return right

# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# print(binary(n, m, a))

# def max_wins(N, S):
#     win_hand = {'R': 'P', 'P': 'S', 'S': 'R'}
#     win_count = 0
#     prev_hand = None

#     for i in range(N):
#         current_win_hand = win_hand[S[i]]
        
#         if prev_hand == current_win_hand:
#             # 連続で同じ手の場合は、勝ち手以外の手を出す
#             for hand in win_hand.values():
#                 if hand != current_win_hand:
#                     prev_hand = hand
#                     break
#         else:
#             prev_hand = current_win_hand
#             win_count += 1
    
#     return win_count

# # 入力を受け取る
# n = int(input())
# s = input()

# # 関数の実行
# result = max_wins(n, s)
# print(result)

# def max_wins(N, S):
#     # 高橋くんの勝った回数
#     win_count = 0
    
#     i = 0
#     while i < N:
#         if i + 1 < N and S[i] == S[i + 1]:
#             # 連続する手が同じ場合は1を加算
#             win_count += 1
#             i += 2  # 2つの手をスキップ
#         else:
#             # 連続する手が異なる場合は2を加算
#             win_count += 2
#             i += 2  # 2つの手をスキップ
    
#     # 最後の手が残った場合の処理
#     if i == N - 1:
#         win_count += 1

#     return win_count

# # 入力を受け取る
# n = int(input())
# s = input()

# # 関数の実行
# result = max_wins(n, s)
# print(result)


# import math

# def max_wins(N, S):
#     win_count = 0
#     i = 0
    
#     while i < N:
#         count = 1
#         while i + 1 < N and S[i] == S[i + 1]:
#             count += 1
#             i += 1
#         win_count += math.ceil(count / 2)
#         i += 1
    
#     return win_count

# # 入力を受け取る
# n = int(input())
# s = input()

# # 関数の実行
# result = max_wins(n, s)
# print(result)


# import math

# def max_wins(N, S):
#     # 高橋くんの勝った回数
#     win_count = 0
#     i = 0
    
#     while i < N:
#         # 連続する同じ文字のカウント
#         count = 1
#         while i + 1 < N and S[i] == S[i + 1]:
#             count += 1
#             i += 1
        
#         # 連続する部分の長さを2で割って切り上げた回数を加算
#         win_count += math.ceil(count / 2)
        
#         # # 連続する部分の最後の文字と次の文字が異なる場合
#         # if i + 1 < N and S[i] != S[i + 1]:
#         #     win_count += 1
        
#         i += 1
    
#     return win_count

# # 入力を受け取る
# n = int(input())
# s = input()

# # 関数の実行
# result = max_wins(n, s)
# print(result)

# def max_wins(n, s):
#     win_hand = {'R': 'P', 'P': 'S', 'S': 'R'}
    
#     last_hand = None
#     win_count = 0

#     for i in range(n):
#         aoki_hand = s[i]
#         takahashi_hand = win_hand[aoki_hand]
        
#         if takahashi_hand == last_hand:
#             for hand in ['R', 'P', 'S']:
#                 if hand != last_hand and hand != aoki_hand:
#                     takahashi_hand = hand
#                     break
#         print(takahashi_hand)
#         if takahashi_hand == win_hand[aoki_hand]:
#             win_count += 1
        
#         last_hand = takahashi_hand
    
#     return win_count

# n = int(input())
# s = input().strip()

# result = max_wins(n, s)
# print(result)


def max_wins(n, s):
    win_hand = {'R': 'P', 'P': 'S', 'S': 'R'}
    draw_hand = {'R': 'R', 'P': 'P', 'S': 'S'}
    
    last_hand = None
    win_count = 0

    for i in range(n):
        aoki_hand = s[i]
        takahashi_hand = win_hand[aoki_hand]
        
        if takahashi_hand == last_hand:
            takahashi_hand = draw_hand[aoki_hand]

        if takahashi_hand == win_hand[aoki_hand]:
            win_count += 1
        
        last_hand = takahashi_hand
    
    return win_count

n = int(input())
s = input().strip()

result = max_wins(n, s)
print(result)

