from pprint import pprint
# 入力
N, W = map(int, input().split())
w = [ None ] * (N + 1)
v = [ None ] * (N + 1)
for i in range(1, N+1):
	w[i], v[i] = map(int, input().split())
#w[i]は重さ,v[i]は価値
 
# 動的計画法
dp = [ [ -99] * (W + 1) for i in range(N + 1) ]
dp[0][0] = 0
for i in range(1, N+1):
	for j in range(0,W+1):
		if j < w[i]:
			dp[i][j] = dp[i-1][j]
		if j >= w[i]:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            # 一つ上の段の値か、最初(それか重さの合計している途中のもの)に価値を加えた値どっちが大きいか
 

# 出力
pprint(dp)
print(max(dp[N]))