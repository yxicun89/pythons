# H,W = map(int,input().split())
# X = [list(map(int, input().split())) for _ in range(H)]
# Q=int(input())
# QS = [list(map(int, input().split())) for _ in range(Q)]
# A=[r[0] for r in QS]
# B=[r[1] for r in QS]
# C=[r[2] for r in QS]
# D=[r[3] for r in QS]
# # print(X)
# # print(A) A~Cで行 B~Dで列
# Z=X
# #横方向の累積和
# for i in range(H):
#     for j in range(1,W):
#         Z[i][j]=Z[i][j-1]+X[i][j]
# # 縦方向の累積和
# for i in range(1,H):
#     for j in range(W):
#         Z[i][j]=Z[i-1][j]+X[i][j]
# # A->0 B->1 C->2 D->3
# # for i in range(Q):
# #     print(Z[C[i]][D[i]]+Z[A[i]-1][B[i]-1]-Z[A[i]-1][D[i]]-Z[C[i]][B[i]-1])
# print(Z)
# for i in range(Q):
# 	print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])

# 入力（前半）
H, W = map(int, input().split())
X = [ None ] * (H)
Z = [ [ 0 ] * (W + 1) for i in range(H + 1) ]
for i in range(H):
	X[i] = list(map(int, input().split()))

# 入力（後半）
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
	A[i], B[i], C[i], D[i] = map(int, input().split())

# 配列 Z は既に初期化済み
# 横方向に累積和をとる
# X[i-1][j-1] などになっているのは、配列が 0 番目から始まるため
for i in range(1, H+1):
	for j in range(1, W+1):
		Z[i][j] = Z[i][j-1] + X[i-1][j-1]

# 縦方向に累積和をとる
for j in range(1, W+1):
	for i in range(1, H+1):
		Z[i][j] = Z[i-1][j] + Z[i][j]

print(Z)
print(X)
# 答えを求め
for i in range(Q):
	print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])