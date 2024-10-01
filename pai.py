# def longest_consecutive_sequence(arr):
#     if not arr or not arr[0]:
#         return 0
    
#     N = len(arr)
#     max_length = 0
    
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
#     memo = [[-1] * N for _ in range(N)]
    
#     def dfs(x, y):
#         if memo[x][y] != -1:
#             return memo[x][y]
        
#         max_len = 1
        
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
#                 max_len = max(max_len, 1 + dfs(nx, ny))
        
#         memo[x][y] = max_len
#         return max_len
    
#     for i in range(N):
#         for j in range(N):
#             max_length = max(max_length, dfs(i, j))
    
#     return max_length

# n = int(input())  
# arr = [list(input()) for _ in range(n)]

# arr = [[int(x) for x in y] for y in arr]

# print(longest_consecutive_sequence(arr))




# N = int(input())

# A = [0] * N
# B = [0] * N

# for i in range(N):
#     A[i],B[i] = map(int,input().split())

# ans = [0] * max(max(A),max(B))

# for i in range(N):
#     for j in range(A[i]-1,B[i]):
#         ans[j] = 1


# count = 0
# for i in ans:
#     if i == 1:
#         count += 1
#     else:
#         count = 0
# print(count)
# # print(sum(ans))





# N = int(input())

# jobs = []
# for _ in range(N):
#     A, B = map(int, input().split())
#     jobs.append((A, B))

# max_end_date = max(jobs, key=lambda x: x[1])[1]
# ans = [0] * (max_end_date + 1)

# for start, end in jobs:
#     for j in range(start, end + 1):
#         ans[j] = 1

# max_streak = 0
# current_streak = 0
# for i in ans:
#     if i == 1:
#         current_streak += 1
#         max_streak = max(max_streak, current_streak)
#     else:
#         current_streak = 0

# print(max_streak)





# def max_score(H, W, board):
#     dp = [[0] * (W + 1) for _ in range(H + 1)]

#     for i in range(1, H + 1):
#         for j in range(1,W + 1):
#             score = board[i - 1][j - 1]

#             for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]:
#                 if 1 <= ni <= H and 1 <= nj <= W:
#                     score = max(score, board[i - 1][j - 1] + dp[ni][nj])
            
#             dp[i][j] = score
#     return max(dp[H])

# H, W = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(H)]

# print(max_score(H, W, board))





# S=input()

# if len(S) > 10:
#     print(len(S) - 10)
# else:
#     print(0)






# def swapcase(string: str) -> str:
#     return "".join(
#         char.lower() if char.isupper() else char.upper()
#         for char in string
#     )

# Rule = list(input())
# S = list(input())

# for i in range(len(S)):
#     if S[i] not in Rule:
#         S[i] = S[i].swapcase()

# S="".join(S)
# print(S)





# def find_best_seats(N, H, W, P, Q, reserved_seats):
#     best_seat = (P, Q)
#     reserved_set = set(reserved_seats)
    
#     seats = []
#     for p in range(H):
#         for q in range(W):
#             if (p, q) not in reserved_set:
#                 distance = abs(p - best_seat[0]) + abs(q - best_seat[1])
#                 seats.append(((p, q), distance))
    
#     min_distance = min(seats, key=lambda x: x[1])[1]
    
#     best_seats = [seat for seat, distance in seats if distance == min_distance]
    
#     return best_seats

# N, H, W, P, Q = map(int, input().split())
# reserved_seats = [tuple(map(int, input().split())) for _ in range(N)]

# best_seats = find_best_seats(N, H, W, P, Q, reserved_seats)
# for seat in best_seats:
#     print(seat[0], seat[1])






# N,M=map(int,input().split())
# num = [list(map(int, input().split())) for _ in range(N)]
# X=int(input())
# t = [list(map(int, input().split())) for _ in range(X)]


# count=0

# current_l=1
# current_r=1

# for i in range(X):
#     if t[i][0] != current_l:
#         current_l = t[i][0]

#     count += abs(num[t[i][0]-1][t[i][1]-1]-num[current_l - 1][current_r - 1])
#     current_l = t[i][0]
#     current_r = t[i][1]

# print(count)






# def read_input():
#     H, W= map(int, input().split())
#     num = [input() for _ in range(N)]

#     H = int(data[0])
#     W = int(data[1])
#     grid = []
#     for i in range(H):
#         grid.append(list(data[2 + i]))
#     return H, W, grid

# def dfs(grid, visited, x, y):
#     H, W = len(grid), len(grid[0])
#     stack = [(x, y)]
#     visited[x][y] = True
#     count = 0

#     while stack:
#         cx, cy = stack.pop()
#         count += 1
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
#                 visited[nx][ny] = True
#                 stack.append((nx, ny))
#     return count

# def initial_lake_size(grid, H, W):
#     visited = [[False] * W for _ in range(H)]
#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '#' and not visited[i][j]:
#                 return dfs(grid, visited, i, j)
#     return 0

# def is_valid_to_build(grid, H, W, initial_size):
#     valid_positions = 0

#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '#':
#                 grid[i][j] = '.'
#                 visited = [[False] * W for _ in range(H)]
#                 new_lake_size = 0
#                 for x in range(H):
#                     for y in range(W):
#                         if grid[x][y] == '#' and not visited[x][y]:
#                             new_lake_size = dfs(grid, visited, x, y)
#                             break
#                     if new_lake_size > 0:
#                         break
#                 if new_lake_size == initial_size:
#                     valid_positions += 1
#                 grid[i][j] = '#'
    
#     return valid_positions

# def main():
#     H, W, grid = read_input()
#     initial_size = initial_lake_size(grid, H, W)
#     valid_positions = is_valid_to_build(grid, H, W, initial_size)
#     print(valid_positions)

# if __name__ == "__main__":
#     main()







# def dfs(grid, visited, x, y):
#     H, W = len(grid), len(grid[0])
#     stack = [(x, y)]
#     visited[x][y] = True
#     count = 0

#     while stack:
#         cx, cy = stack.pop()
#         count += 1
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
#                 visited[nx][ny] = True
#                 stack.append((nx, ny))
#     return count

# def initial_lake_size(grid, H, W):
#     visited = [[False] * W for _ in range(H)]
#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '#' and not visited[i][j]:
#                 return dfs(grid, visited, i, j)
#     return 0

# def is_valid_to_build(grid, H, W, initial_size):
#     valid_positions = 0

#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '#':
#                 grid[i][j] = '.'
#                 visited = [[False] * W for _ in range(H)]
#                 new_lake_size = 0
#                 for x in range(H):
#                     for y in range(W):
#                         if grid[x][y] == '#' and not visited[x][y]:
#                             new_lake_size = dfs(grid, visited, x, y)
#                             break
#                     if new_lake_size > 0:
#                         break
#                 if new_lake_size == initial_size:
#                     valid_positions += 1
#                 grid[i][j] = '#'
    
#     return valid_positions

# def main():
#     H, W = map(int, input().split())
#     grid = [input() for _ in range(H)]
#     grid = [list(i) for i in grid]
#     initial_size = initial_lake_size(grid, H, W)
#     valid_positions = is_valid_to_build(grid, H, W, initial_size)
#     print(valid_positions)

# if __name__ == "__main__":
#     main()






# def is_within_bounds(x, y, H, W):
#     return 0 <= x < H and 0 <= y < W

# def dfs(x, y, grid, visited, exclude):
#     stack = [(x, y)]
#     visited.add((x, y))
#     while stack:
#         cx, cy = stack.pop()
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = cx + dx, cy + dy
#             if is_within_bounds(nx, ny, len(grid), len(grid[0])) and grid[nx][ny] == '#' and (nx, ny) != exclude and (nx, ny) not in visited:
#                 visited.add((nx, ny))
#                 stack.append((nx, ny))

# def is_connected_lake(grid, exclude=None):
#     H, W = len(grid), len(grid[0])
#     visited = set()
#     found_lake = False
    
#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '#' and (i, j) != exclude and (i, j) not in visited:
#                 if found_lake:
#                     return False
#                 dfs(i, j, grid, visited, exclude)
#                 found_lake = True
    
#     return found_lake

# def count_buildable_areas(H, W, grid):
#     buildable_count = 0
#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '#':
#                 if is_connected_lake(grid, exclude=(i, j)):
#                     buildable_count += 1
#             else:
#                 buildable_count += 1
    
#     return buildable_count

# H, W = map(int, input().strip().split())
# grid = [input().strip() for _ in range(H)]

# result = count_buildable_areas(H, W, grid)

# print(result)








# N,D = map(int, input().split())
# X,Y= map(int, input().split())
# x=[0]*N
# y=[0]*N
# count=0
# for i in range(N):
#     x[i],y[i] = map(int, input().split())

#     dif=abs(x[i]-X) + abs(y[i] - Y)
#     if dif <= D:
#         count+=1

# print(count)






# import math

# N=int(input())
# M=int(input())

# gcd = math.gcd(N,M)

# if gcd == 1:
#     print("yes")
# else:
#     print("no")






# s = input()

# for i in s:
#     if i in "aiueoAIUEO":
#         s = s.replace(i,'')
# print(s)






# n,x,y=map(int,input().split())

# for i in range(1,n+1):
#     if (i % x == 0) and (i % y == 0):
#         print("AB") 
#     elif i % x == 0:
#         print("A")
#     elif i % y == 0:
#         print("B")
#     else:
#         print("N")








# n,k = map(int,input().split())
# b = [list(map(int, input().split())) for _ in range(n)]
# c = list(map(int,input().split()))

# row = [0] * n
# col = [0] * n
# l_cross = 0
# r_cross = 0
# result = 0
# for i in range(len(b)):
#     for j in range(len(b[0])):
#         if b[i][j] in c or b[i][j] == 0:
#             row[i] += 1
#             col[j] += 1
#             if i == j:
#                 l_cross += 1
#             if i + j == n - 1:
#                 r_cross += 1
#             if row[i] == n or col[j] == n:
#                 result += ((row[i] == n) + (col[j] == n)) 
#             if l_cross == n:
#                 result += 1
#                 l_cross = 0
#             if r_cross == n:
#                 result += 1
#                 r_cross = 0
        

# print(result)




# N,L=map(int,input().split())
# x = [int(input()) for _ in range(N)]

# for i in x:
#     if L > i:
#         L += int(i/2)
#     elif L < i:
#         L = L // 2
# print(L)




# 0 0 0 0 0 
# 2 0 0 0 0 
# 2 0 2 0 0
# 2 0 0 0 3

# N,M=map(int,input().split())
# num_list = [list(map(int, input().split())) for _ in range(M)]
# train=[1]*N

# for i in num_list:
#     train[i[0]-1] += train[i[1]-1]


# maxlist = [i for i, x in enumerate(train) if x == max(train)]

# for i in maxlist:
#     print(i+1)





# N,M=map(int,input().split())
# num_list = [int(input()) for _ in range(N-1)]
# sum=0

# for i in num_list:
#     if i < M:
#         sum += i

# print(sum)


# 3 3
# 5 5 5
# 6 5 3

# 0 0 0
# 5 1 0
# 5 1 5
# 8 1 5 合計人数だからiが末尾に行ったら先頭に戻ってゴンドラは空のが来る


# N,M=map(int,input().split()) #ゴンドラ数,グループ数
# A = [int(input()) for _ in range(N)] #Ai人乗れるゴンドラ
# B = [int(input()) for _ in range(M)] #グループの人数

# gon = [0] * N

# for i in range(M):
#     if gon[i] < A[i]:
#         gon[i] += B[i]


# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# rides = 0  
# empty_seats = K  

# for group_size in A:
#     if group_size <= empty_seats:
#         empty_seats -= group_size 

#     else:
#         rides += 1  
#         empty_seats = K - group_size 

# print(rides+1)




# N,K=map(int,input().split())

# # num_ID = [input().split() for _ in range(N)]
# dic={}
# for _ in range(N):
#     key,value = input().split()
#     dic[key]=value

# S = [input().split() for _ in range(K)]

# for i in S:
#     if i[0] == "join":
#         dic[i[1]] = i[2]
#     elif i[0] == "leave":
#         del dic[i[1]]
#     else:
#         print(dic[str(i[1])])





# N,K=map(int,input().split())

# # num_ID = [input().split() for _ in range(N)]
# # name={}
# # for _ in range(N):
# #     key,value = input().split()
# #     name[key]=value
# name = [input() for _ in range(N)]

# S = [input().split() for _ in range(K)]

# for i in S:
#     if i[0] == "leave":
#         name.remove(i[1])
#     elif i[0] == "join":
#         name.append(i[1])
#     else:
#         if len(name) != 0:
#             name.sort()
#             for j in name:
#                 print(j)




# ax1,ay1,bx1,by1,cx1,cy1,dx1,dy1,ax2,ay2,bx2,by2,cx2,cy2,dx2,dy2 = map(int,input().split())

# #長方形1の右上の点
# max_x1=max(ax1,bx1,cx1,dx1) 
# max_y1=max(ay1,by1,cy1,dy1) 
# #長方形1の左下の点
# min_x1=min(ax1,bx1,cx1,dx1)
# min_y1=min(ay1,by1,cy1,dy1)
# #長方形2の右上の点
# max_x2=max(ax2,bx2,cx2,dx2)
# max_y2=max(ay2,by2,cy2,dy2)
# #長方形2の左下の点
# min_x2=min(ax2,bx2,cx2,dx2)
# min_y2=min(ay2,by2,cy2,dy2)

# if (min_x1 < min_x2 and max_x1 > max_x2 and min_y1 < min_y2 and max_y1 > max_y2):
#     print("FALSE")
# elif (min_x2 < min_x1 and max_x2 > max_x1 and min_y2 < min_y1 and max_y2 > max_y1):
#     print("FALSE")
# elif ((max(min_x1,min_x2) <= min(max_x1,max_x2)) and (max(min_y1,min_y2) <= min(max_y1,max_y2))):
#     print("TRUE")
# else :
#     print("FALSE")





# l, r = map(int, input().split())
# m = int(input())
# n = list(map(int, input().split()))

# monsters = set(range(l, r + 1))

# for ni in n:
#     monsters -= set(range(ni, r + 1, ni)

# print(len(monsters))

# l, r = map(int, input().split())
# m = int(input())
# n = list(map(int, input().split()))

# monsters = set(range(l, r + 1))

# for ni in n:
#     monsters -= set(range(ni, r + 1, ni))

# print(len(monsters))


# import math
# from itertools import combinations

# def count_mult(x, l, r):
#     if x > r:
#         return 0
#     return r // x - (l - 1) // x

# def lcm(numbers):
#     return math.lcm(*numbers)


# def erato(n, l, r):

#     m = len(n)
#     count = 0

#     for i in range(1, m + 1):
#         comb = combinations(n, i)
#         for c in comb:
#             lcm_c = lcm(c)
#             if i % 2 == 1: 
#                 count += count_mult(lcm_c, l, r)
#             else: 
#                 count -= count_mult(lcm_c, l, r)
    
#     return count


# def main():
#     l, r = map(int, input().split())
#     m = int(input())
#     n = list(map(int, input().split()))
#     total = r - l + 1
#     exclude = erato(n, l, r)
#     remain = total - exclude
#     print(remain)


# if __name__ == "__main__":
#     main()


# # ２文字の語尾と誤答を共有する単語の長さの最大値
# def check(prev,next):
#     if prev[-2:] == next[:2]:
#         return prev + next[2:]
#     else:
#         return ""

# n=int(input())
# s=[input() for _ in range(n)]
 
# # new_s=[i for i in s if len(i) >= 2]
# ans=s[0]

# for i in range(n-1):
#     if len(ans) < len(check(s[i],s[i+1])):
#         ans = check(s[i],s[i+1])

# if ans == s[0]:
#     print(-1)
# else:
#     print(len(ans))


# n = int(input())
# s = [input() for _ in range(n)]

# from collections import defaultdict

# start_dict = defaultdict(int)
# end_dict = defaultdict(int)
# word_length = defaultdict(int)

# for word in s:
#     start = word[:2]
#     end = word[-2:]
#     start_dict[start] = max(start_dict[start], len(word))
#     end_dict[end] = max(end_dict[end], len(word))
#     word_length[word] = len(word)

# max_length = -1
# for end, length in end_dict.items():
#     if end in start_dict:
#         max_length = max(max_length, length + start_dict[end] - 2)

# print(max_length)


# n = int(input())
# s = [input() for _ in range(n)]

# from collections import defaultdict

# start_dict = defaultdict(int)
# end_dict = defaultdict(int)

# for word in s:
#     start = word[:2]
#     end = word[-2:]
#     start_dict[start] = max(start_dict[start], len(word))
#     end_dict[end] = max(end_dict[end], len(word))

# max_length = -1
# for end, end_length in end_dict.items():
#     if end in start_dict:
#         start_length = start_dict[end]
#         if end_length != start_length: 
#             max_length = max(max_length, end_length + start_length)
#         else:  
#             if len([word for word in s if word[:2] == end]) > 1 or len([word for word in s if word[-2:] == end]) > 1:
#                 max_length = max(max_length, end_length + start_length)

# print(max_length)



#あんぱんち
from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]

start_dict = defaultdict(int)
end_dict = defaultdict(int)

for word in s:
    start = word[:2]
    end = word[-2:]
    start_dict[start] = max(start_dict[start], len(word))
    end_dict[end] = max(end_dict[end], len(word))

max_length = -1

if n==2:
    if s[0][-2:] == s[1][:2]:
        max_length=len(s[0]+s[1])-2
else:
    for end, end_length in end_dict.items():
        if end in start_dict:
            start_length = start_dict[end]
            if end_length != start_length: 
                max_length = max(max_length, end_length + start_length - 2)
            else:  
                if len(s) == 2 or len([word for word in s if word[:2] == end]) > 1 or len([word for word in s if word[-2:] == end]) > 1:
                    max_length = max(max_length, end_length + start_length - 2)

print(max_length)

