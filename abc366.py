# n,t,a=map(int,input().split())

# if abs(t-a) < (n-(t+a)):
#     print("No") 
# else:
#     print("Yes")


# def vertical_strings(n, strings):
#     M = max(len(s) for s in strings)

#     result = [""] * M

#     for i in range(M):
#         for j in range(n):
#             if i < len(strings[j]):
#                 result[i] += strings[j][i]
#             else:
#                 result[i] += '*'

    
#     result = [line[::-1] for line in result]
#     for i in range(len(result)):
#         while result[i].endswith('*'):
#             result[i] = result[i][:-1]

#     return result

# n = int(input())
# s = [input() for _ in range(n)]

# result = vertical_strings(n, s)
# for line in result:
#     print(line)


# bag = {}

# Q = int(input())

# for _ in range(Q):
#     query = input().split()
    
#     if query[0] == "1":
#         x = int(query[1])
#         if x in bag:
#             bag[x] += 1
#         else:
#             bag[x] = 1
    
#     elif query[0] == "2":
#         x = int(query[1])
#         if x in bag:
#             bag[x] -= 1
#             if bag[x] == 0:
#                 del bag[x]
    
#     elif query[0] == "3":
#         print(len(bag))

n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n*n)]

A = [[[0] * n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j] = num_list[i * n + j]

S = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            S[x][y][z] = A[x-1][y-1][z-1] + S[x-1][y][z] + S[x][y-1][z] + S[x][y][z-1] \
                         - S[x-1][y-1][z] - S[x-1][y][z-1] - S[x][y-1][z-1] \
                         + S[x-1][y-1][z-1]

q = int(input())
l = [list(map(int, input().split())) for _ in range(q)]

results = []
for i in range(q):
    Lxi, Rxi, Lyi, Ryi, Lzi, Rzi = l[i]
    result = S[Rxi][Ryi][Rzi] \
             - S[Lxi-1][Ryi][Rzi] - S[Rxi][Lyi-1][Rzi] - S[Rxi][Ryi][Lzi-1] \
             + S[Lxi-1][Lyi-1][Rzi] + S[Lxi-1][Ryi][Lzi-1] + S[Rxi][Lyi-1][Lzi-1] \
             - S[Lxi-1][Lyi-1][Lzi-1]
    results.append(result)

for res in results:
    print(res)
