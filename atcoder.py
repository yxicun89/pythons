def calc_next(S):
    n = len(S)
    res = [[n] * 26 for _ in range(n + 1)] #26個のアルファベット*単語数
    for i in range(n - 1, -1, -1):
        # print(S[i])
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][ord(S[i]) - ord('a')] = i
        # 被るほど最初の方が小さくなっていく（登場順番）1個後ろの文字の結果を一個前に渡していく。
        # 文字の末尾から見ていくことで一番左に最初の文字ができる
        # print(res)
    print(res[0])
    # print(res[1])
    return res

def main():
    S = input().strip()
    n = len(S)
    
    # print(S[1])

    next = calc_next(S)
    # print(next)

    dp = [0] * (n + 1)
    dp[0] = 1 
    
    for i in range(n): #1文字目~最後まで
        for j in range(26): #a~z
            if next[i][j] >= n: #ありえない部分文字列
                continue
            print(next[i][j],i,j)
            dp[next[i][j] + 1] += dp[i] 
            #nyannyanの場合最初のnの次のnが出現する位置で発動してる。
            print(dp)

    print(dp)
    res = 0
    for i in range(n + 1):
        res += dp[i]

    print(res-1)

if __name__ == "__main__":
    main()


# N=int(input())
# M=int(input())

# print(2*M - N)


# n = int(input()) 
# num_list = [int(input()) for _ in range(n)]

# num_sort=sorted(num_list,reverse=True)
# dic={}
# for i in range(n):
#     dic[str(num_sort[i])] = 0


# for i in range(n):
#     if dic[str(num_sort[i])] == 0:
#         dic[str(num_sort[i])] = i+1

# ans=[]
# for i in num_list:
#     ans.append(dic[str(i)])

# for i in ans:
#     print(i)

# num_list = list(map(int,input().split())) 
# S=list(input())
# ans=''
# for i in S:
#     if num_list[ord(i) - ord('a')] > 0:
#         ans+=i
#         num_list[ord(i) - ord('a')] -= 1

# print(ans)


# n = int(input())
# str_list = [list(input().split()) for _ in range(n)]

# count=0

# for i in str_list:
#     if (i[0]=="G" and i[1] =="C") or (i[0]=="C" and i[1] =="P") or (i[0]=="P" and i[1] =="G"):
#         count += 1
# print(count)

# n = int(input()) 
# num_list = [list(map(int, input().split())) for _ in range(n)]

# maxT=0
# minT=100

# for i in num_list:
#     sum = i[0] + i[1] + (24-i[2])
#     maxT=max(sum,maxT)
#     minT=min(sum,minT)

# print(minT)
# print(maxT)

# n,k=map(int,input().split())
# b = [list(map(int, input().split())) for _ in range(n)]
# c = list(map(int, input().split()))


# 行、列、対角線のカウント用リストを初期化
# row_count = [0] * N
# col_count = [0] * N
# diag1_count = 0
# diag2_count = 0

# ビンゴ達成ターンをチェック
# result = 0  # ビンゴが達成されなかった場合の初期値

# for turn in range(T):
#     num = A[turn]
#     i = (num - 1) // N
#     j = (num - 1) % N
    
#     # 行、列、対角線のカウントを更新
#     row_count[i] += 1
#     col_count[j] += 1
#     if i == j:
#         diag1_count += 1
#     if i + j == N - 1:
#         diag2_count += 1
    
#     # ビンゴが達成されたかチェック
#     if row_count[i] == N or col_count[j] == N or diag1_count == N or diag2_count == N:
#         result = turn + 1  # 0-indexedなので1を足す
#         break  # 最初のビンゴ達成ターンでループを終了

# # 結果の表示
# print(result)
