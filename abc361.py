# n,k,x=map(int,input().split())
# a = list(map(int,input().split()))
# a.insert(k,x)
# print(*a)

# def is_intersecting(a, b, c, d, e, f, g, h, i, j, k, l):
#     min_x1, max_x1 = min(a, d), max(a, d)
#     min_y1, max_y1 = min(b, e), max(b, e)
#     min_z1, max_z1 = min(c, f), max(c, f)
    
#     min_x2, max_x2 = min(g, j), max(g, j)
#     min_y2, max_y2 = min(h, k), max(h, k)
#     min_z2, max_z2 = min(i, l), max(i, l)
    
#     x_overlap = max_x1 > min_x2 and max_x2 > min_x1
#     y_overlap = max_y1 > min_y2 and max_y2 > min_y1
#     z_overlap = max_z1 > min_z2 and max_z2 > min_z1
    
#     return x_overlap and y_overlap and z_overlap

# a, b, c, d, e, f = map(int, input().split())
# g, h, i, j, k, l = map(int, input().split())

# if is_intersecting(a, b, c, d, e, f, g, h, i, j, k, l):
#     print("Yes")
# else:
#     print("No")


# def min_difference_after_removal(N, K, A):
#     M = N - K
#     min_diff = float('inf')
    
#     for i in range(N - M + 1):
#         current_subarray = A[i:i + M]
#         max_val = max(current_subarray)
#         min_val = min(current_subarray)
#         diff = max_val - min_val
#         if diff < min_diff:
#             min_diff = diff
    
#     return min_diff


# n,k=map(int,input().split())
# a = list(map(int,input().split()))
# a.sort()
# count = 0

# while count < k:
#     if (a[1] - a[0]) < (a[len(a)-1] - a[len(a)-2]):
#         a.pop(-1)
#     else:
#         a.pop(0)

#     count += 1

# print(max(a)-min(a))

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()

# min_difference = float('inf')
# for i in range(k + 1):
#     current_difference = a[n - k + i - 1] - a[i]
#     if current_difference < min_difference:
#         min_difference = current_difference

# print(min_difference)


def min_operations(N, S, T):
    # 初期状態と目標状態が同じであれば操作は不要
    if S == T:
        return 0

    # 白と黒の石の数が一致しない場合は不可能
    if S.count('W') != T.count('W') or S.count('B') != T.count('B'):
        return -1

    # 各色の石の初期位置と目標位置を取得
    initial_positions_W = [i for i in range(N) if S[i] == 'W']
    initial_positions_B = [i for i in range(N) if S[i] == 'B']
    target_positions_W = [i for i in range(N) if T[i] == 'W']
    target_positions_B = [i for i in range(N) if T[i] == 'B']

    # 操作回数のカウント
    operations = 0

    # 白の石の移動に必要な操作回数を計算
    for initial, target in zip(initial_positions_W, target_positions_W):
        operations += abs(initial - target)

    # 黒の石の移動に必要な操作回数を計算
    for initial, target in zip(initial_positions_B, target_positions_B):
        operations += abs(initial - target)

    return operations


n=int(input())
s=input()
t=input()
print(min_operations(n, s, t))  

