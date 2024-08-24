# n, k = input().split()
# n = int(n, 8) #8進数を10進数に変換してる
# print(n)

#  n = int(ans[::-1], 8)　#9進数に変換したものを逆順に取り出すことで、9進数を表していて、それをまた8進数に戻す。これはk回操作を行うため。

# def convertToBase9(n):
#     if n == 0:
#         return '0'
#     digits = ''
#     while n:
#         digits = str(n % 9) + digits
#         n //= 9
#     return digits

# def main():
#     N, K = map(int, input().split())
#     for _ in range(K):
#         N = convertToBase9(N).replace('8', '5')
#         N = int(N, 9)  # 9進数の文字列を10進数の整数に変換
#     print(N)

# n, m = map(int, input().split())
# adj_list = [[] for _ in range(n)]

# for i in range(m):
#     a, b = map(int, input().split())
#     adj_list[a-1].append(b)
#     adj_list[b-1].append(a)

# count = 0
# for i in range(n):
#     if all(j >= i for j in adj_list[i]) and len(adj_list[i]) == 1:
#         count += 1
# print(adj_list)
# print(count)

# N, M = map(int, input().split())
# G = [[]for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a-1].append(b-1)
#     G[b-1].append(a-1)

# ans = 0
# for nd in range(N):
#     cnt = 0
#     for nxt in G[nd]:
#         if nxt < nd:
#             cnt += 1
#         elif nxt > nd:
#             break
#     if cnt == 1:
#         ans += 1
# print(ans)

# N, M = map(int, input().split())
# G = [[]for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     a-=1
#     b-=1
#     G[a].append(b)
#     G[b].append(a)
# ans = 0
# for i in range(N):
#     G[i].sort()

# for nd in range(N):
#     cnt = 0
#     for nxt in G[nd]:
#         if nxt < nd:
#             cnt += 1
#         elif nxt > nd:
#             break
#     if cnt == 1:
#         ans += 1
# print(ans)

# print(G)

# n, m = map(int, input().split())

# list = [[] for i in range(n)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     list[a-1].append(b)
#     list[b-1].append(a)

# ans = 0
# for i in range(n):
#     count = 0
#     for j in range(len(list[i])):
#         if list[i][j] < i+1:
#             count += 1
#     if count == 1:
#         ans += 1
        
# print(ans)

# n,k = map(int,input().split())
# for i in range(k):
#     s = str(n)
#     a = 0
#     for j in range(len(s)):
#         a += int(s[-j - 1]) * pow(8,j)
#         # print(i)
#     # print(a)
#     b = []
#     while a != 0:
#         b.append(str(a % 9))
#         a //= 9
#     for k in range(len(b)):
#         if b[k] == "8":b[k] = "5"
#         # print(i)
#     # print(b)
#     n = "".join(b[::-1])
#     if n == "":n = 0
# print(n)


for i in range(5):
    for i in range(4):
        print(i*i)