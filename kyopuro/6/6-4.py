# 入力
# A は (終了時刻, 開始時刻) になっていることに注意 [終了時刻の昇順にソートするため]
N = int(input())
A = []
for i in range(N):
	l, r = map(int, input().split())
	A.append([r, l])

# ソート
A.sort()　#rightをソートするために[r,l]にしてる、その後貪欲方法
# print(A)

# 終了時刻の早いものから貪欲に取っていく（CurrentTime は現在時刻）
CT = 0
Answer = 0
for i in range(N):
	if CT <= A[i][1]:
		CT = A[i][0]
		Answer += 1

# 出力
print(Answer)