# N=int(input())
# C=""
# for i in range(1,N+1):
#     if i % 3 == 0:
#         C+="x"
#     else:
#         C+="o"
# print(C)






# import math

# N=int(input())
# X=[0] * N
# Y=[0] * N
# for i in range(N):
#     X[i],Y[i]=map(int,input().split())

# ans = [0,1]
# cnt=1
# for j in range(N):
#     for t in range(N):
#         t=math.sqrt(pow(X[t]-X[j],2) + pow(Y[t] - Y[j],2))
#         if t > ans[0]:
#             ans[0] = t
#             ans[1] = cnt
#             print(ans)
#         cnt=1
#     print(ans[1])
#     ans=[0,1]






# S=input()
# if S[0:3]=="ABC" and int(S[3:6])!= 316 and int(S[3:6]) != 0 and int(S[3:6]) < 350:
#     print("Yes")
# else:
#     print("No")






# N,Q=map(int,input().split())
# num_list = list(map(int, input().split()))

# H=[1]*N
# for i in range(Q):
#     if H[num_list[i]-1] == 1:
#         H[num_list[i]-1] = 0
#     else:
#         H[num_list[i]-1] = 1

# print(sum(H))







# N,X,Y,Z=map(int,input().split())

# if X-Y < 0 and X < Z and Z < Y:
#     print("Yes")
# elif X-Y > 0 and X > Z and Z > Y:
#     print("Yes")
# else:
#     print("No")






# 全探索すぎた
# S=input()
# T=input()
# ans = [0] * len(T)
# count=0

# # while count == len(S):
# for j in range(len(S)):
#     for i in range(len(T)):
#         if ans[i] != 1 and T[i] == S[j]:
#             ans[i] = 1
#             count += 1
#             break

# print(count)
# print(ans)
# for i in range(len(ans)):
#     if ans[i] == 1:
#         print(i+1)






# s = input()
# t = input()

# start = 0
# ans = [0]*len(s)
# count = 0

# for i in range(0, len(s)):
  
#   for j in range(start, len(t)):
#     if s[i] == t[j]:
#       start = j+1
#       ans[count] = j+1
#       count += 1
#       break
# print(*ans)







# N=int(input())
# num_list = list(map(int, input().split()))  
# flag = 0
# for i in range(1,N):
#     if num_list[i] > num_list[0]:
#         print(i+1)
#         flag = 1
#         break
# if flag == 0:
#     print(-1)






# N,K = map(int,input().split())
# num_list = list(map(int, input().split()))  



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








#総和を割るんじゃなくて各々の数字を割ってからやる

# N=int(input())
# A = list(map(int, input().split()))
# sum = 0

# for i in range(N-1):
#     for j in range(i+1,N):
#         # if i != j:
#         sum = sum + ((A[i] % (10 ** 8)) + A[j] % (10 ** 8)) % (10 ** 8)

# print(sum) 



# N = int(input())
# A = list(map(int, input().split()))

# counts = {}
# for num in A:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1

# total_sum = sum(A) * N

# for num, count in counts.items():
#     total_sum -= num * count

# print(total_sum % (10 ** 8))

# H=int(input())

# count = 0
# plant = 0

# while plant <= H:
#     plant += 2**count
#     count += 1

# print(count)

# N=int(input())

# S=[''] * N
# C=[''] * N

# for i in range(N):
#     S[i],C[i] = input().split()

# C = [int(x) for x in C]
# S.sort()
# print(S[sum(C) % N])


# N=int(input())

# A=[0] * N
# C=[0] * N

# for i in range(N):
#     A[i],C[i] = map(int,input().split())


# def filter_cards(N, cards):
#     # 強さで降順、同じ強さの場合はコストで昇順にソート
#     cards_sorted = sorted(cards, key=lambda x: (-x[0], x[1]))
    
#     # フィルタリングされたカードを保持するリスト
#     filtered_cards = []
    
#     # 現在の最小コストを初期化
#     current_min_cost = float('inf')
    
#     for strength, cost in cards_sorted:
#         # 現在の最小コストよりも小さい場合のみカードを追加
#         if cost < current_min_cost:
#             filtered_cards.append((strength, cost))
#             current_min_cost = cost
    
#     # フィルタリングされたカードを元の入力順に戻す
#     filtered_cards.sort(key=lambda x: (cards.index(x), x[0], x[1]))
    
#     return filtered_cards

# if __name__ == "__main__":
#     import sys
#     input = sys.stdin.read
#     data = input().splitlines()
    
#     N = int(data[0])
#     cards = []
    
#     for i in range(1, N + 1):
#         A, C = map(int, data[i].split())
#         cards.append((A, C))
    
#     result = filter_cards(N, cards)
    
#     # 出力は捨てられなかったカードを元の入力順に戻す
#     for strength, cost in result:
#         print(strength, cost)


# A,B=map(int, input().split())

# if A != B:
#     print(6-A-B)
# else:
#     print(-1)


# N,M=map(int, input().split())

# A=list(map(int, input().split()))
# B=list(map(int, input().split()))
# C=A+B
# C.sort()
# flag=0

# for i in range(len(C)-1):
#     if C[i] in A and C[i+1] in A:
#         flag=1

# if flag ==1:
#     print("Yes")
# else:
#     print("No")

# def bingo_turn(N, T, A):
#     row_count = [0] * N
#     col_count = [0] * N
#     diag1_count = 0
#     diag2_count = 0

#     for turn in range(T):
#         num = A[turn]
#         i = (num - 1) // N
#         j = (num - 1) % N
        
#         row_count[i] += 1
#         col_count[j] += 1
#         if i == j:
#             diag1_count += 1
#         if i + j == N - 1:
#             diag2_count += 1
        
#         if row_count[i] == N or col_count[j] == N or diag1_count == N or diag2_count == N:
#             return turn + 1  

#     return -1

# N, T = map(int, input().split())
# A = list(map(int, input().split()))

# result = bingo_turn(N, T, A)
# print(result)


# N, T = map(int, input().split())
# A = list(map(int, input().split()))

# row_count = [0] * N
# col_count = [0] * N
# diag1_count = 0
# diag2_count = 0

# result = -1 

# for turn in range(T):
#     num = A[turn]
#     i = (num - 1) // N
#     j = (num - 1) % N
    
#     row_count[i] += 1
#     col_count[j] += 1
#     if i == j:
#         diag1_count += 1
#     if i + j == N - 1:
#         diag2_count += 1
    
#     if row_count[i] == N or col_count[j] == N or diag1_count == N or diag2_count == N:
#         result = turn + 1 
#         break  

# print(result)

# N,L,R=map(int,input().split())
# num_list=[i+1 for i in range(N)]

# list1=num_list[:L-1] 
# list2=num_list[L-1:R]
# list2.reverse()
# list3=num_list[R::]
# list4=list1+list2+list3
# print(*list4)

# import numpy as np
# n,m = map(int,input().split())

# count = 0

# a=list(map(int, input().split()))

# x = [list(map(int, input().split())) for _ in range(n)]

# xx=np.array(x)

# sum_list=np.sum(xx,axis=0)

# for i in range(len(a)):
#     if a[i] <= sum_list[i]:
#         count+=1

# if count == len(a):
#     print("Yes")
# else:
#     print("No")

# n,m,k = map(int,input().split())
# key = [list(input().split()) for _ in range(m)]
# print(key)

# def count_valid_combinations(N, K, M, tests):
#     valid_count = 0

#     for bits in range(1 << N):
#         valid = True
#         for Ci, keys, result in tests:
#             count_correct_keys = sum((bits >> (key - 1)) & 1 for key in keys)
#             if (result == 'o' and count_correct_keys < K) or (result == 'x' and count_correct_keys >= K):
#                 valid = False
#                 break
        
#         if valid:
#             valid_count += 1

#     return valid_count


# n, m, k = map(int, input().split())
# tests = []
# for _ in range(m):
#     data = input().split()
#     Ci = int(data[0])
#     keys = list(map(int, data[1:1+Ci]))
#     result = data[-1]
#     tests.append((Ci, keys, result))


# print(count_valid_combinations(n, k, m, tests))


# def popcount(x):
#     return bin(x).count('1')

# def sum_popcount(N, M):
#     MOD = 998244353
#     total = 0
#     M %= MOD
#     for k in range(N + 1):
#         k %= MOD
#         total += bin(k & M).count('1')
#         total %= MOD
#     return total

# # 入力の取得
# N, M = map(int, input().split())

# # 結果の出力
# print(sum_popcount(N, M))


# def is_good_sequence(N, K, A):
#     # 数列を昇順にソート
#     A_sorted = sorted(A)
    
#     # 累積和を計算
#     cumulative_sum = 0
#     split_index = -1
    
#     for i in range(N):
#         cumulative_sum += A_sorted[i]
#         if cumulative_sum >= K:
#             split_index = i
#             break
    
#     # split_index が見つからなければ累積和は全て K 未満
#     if split_index == -1:
#         return A_sorted
    
#     # 良い数列を構築
#     good_sequence = A_sorted[:split_index] + A_sorted[split_index:]
    
#     return good_sequence

# # 入力部分
# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)

# print(*result)

# def is_good_sequence(N, K, A):
#     # 数列を昇順にソート
#     A_sorted = sorted(A)
    
#     # 累積和を計算
#     cumulative_sum = 0
#     split_index = -1
    
#     for i in range(N):
#         cumulative_sum += A_sorted[i]
#         if cumulative_sum >= K:
#             split_index = i
#             break
    
#     # 累積和が全て K 未満ならば良い数列にできない
#     if cumulative_sum < K:
#         return "NO"
    
#     # 良い数列を構築
#     good_sequence = A_sorted[:split_index] + A_sorted[split_index:]
    
#     return "YES", good_sequence

# # 入力部分
# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)
# if result == "NO":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))


# def is_good_sequence(N, K, A):
#     A_sorted = sorted(A)
    
#     cumulative_sum = 0
#     for i in range(N):
#         cumulative_sum += A_sorted[i]
#         if cumulative_sum >= K:
#             return "YES", A_sorted[:i+1] + A_sorted[i+1:]
    
#     return "NO"

# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)
# if result == "NO":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))

# def is_good_sequence(N, K, A):
#     # 数列を昇順にソート
#     A_sorted = sorted(A)
    
#     # 累積和を計算
#     cumulative_sum = 0
#     split_index = -1
    
#     for i in range(N):
#         cumulative_sum += A_sorted[i]
#         if cumulative_sum >= K:
#             split_index = i
#             break
    
#     # 累積和が全て K 未満ならば良い数列にできない
#     if split_index == -1:
#         return "NO"
    
#     # 良い数列を構築
#     good_sequence = A_sorted[:split_index+1] + A_sorted[split_index+1:]
    
#     return "YES", good_sequence

# # 入力部分
# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)
# if result == "NO":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))

# def is_good_sequence(N, K, A):
#     A_sorted = sorted(A)
    
#     cumulative_sum = 0
#     less_than_K = []
#     greater_or_equal_K = []
    
#     for a in A_sorted:
#         cumulative_sum += a
#         if cumulative_sum < K:
#             less_than_K.append(a)
#         else:
#             greater_or_equal_K.append(a)
    
#     if not greater_or_equal_K:
#         return "NO"
    
#     good_sequence = less_than_K + greater_or_equal_K
    
#     return "YES", good_sequence

# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)
# if result == "NO":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))

# def is_good_sequence(N, K, A):
#     A_sorted = sorted(A, reverse=True)
    
#     cumulative_sum = 0
#     less_than_K = []
#     greater_or_equal_K = []
    
#     for a in A_sorted:
#         if cumulative_sum < K:
#             less_than_K.append(a)
#         else:
#             greater_or_equal_K.append(a)
#         cumulative_sum += a
    
#     good_sequence = less_than_K + greater_or_equal_K
    
#     cumulative_sum = 0
#     for num in good_sequence:
#         cumulative_sum += num
#         if cumulative_sum >= K:
#             break
#     else:
#         return "No"

#     return "Yes", good_sequence

# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)
# if result == "No":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))

# def is_good_sequence(N, K, A):
#     # 数列を昇順にソート
#     A_sorted = sorted(A)
    
#     # 累積和を計算しながら、K 未満と K 以上の値に分ける
#     cumulative_sum = 0
#     less_than_K = []
#     greater_or_equal_K = []
    
#     for a in A_sorted:
#         cumulative_sum += a
#         if cumulative_sum < K:
#             less_than_K.append(a)
#         else:
#             greater_or_equal_K.append(a)
    
#     # 良い数列を構築
#     good_sequence = less_than_K + greater_or_equal_K
    
#     # 再度累積和を確認して条件を満たすか検証
#     cumulative_sum = 0
#     for num in good_sequence:
#         cumulative_sum += num
#         if cumulative_sum >= K:
#             break
#     else:
#         return "NO"

#     return "YES", good_sequence

# # 入力部分
# N, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = is_good_sequence(N, K, num_list)
# if result == "NO":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))



# N, M = map(int, input().split())
# num_list = list(map(int, input().split()))
# sum=0
# count = 0
# for i in num_list:
#     sum+=i
#     if sum <= M:
#         count+=1
#     else:
#         break

# print(count)


# def create_carpet(level):
#     if level == 0:
#         return ['#']
    
#     prev_carpet = create_carpet(level - 1)
#     size = len(prev_carpet)
#     new_size = size * 3
#     carpet = [['.' for _ in range(new_size)] for _ in range(new_size)]
    
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for x in range(size):
#                 for y in range(size):
#                     carpet[i * size + x][j * size + y] = prev_carpet[x][y]
    
#     return [''.join(row) for row in carpet]

# def print_carpet(carpet):
#     for row in carpet:
#         print(row)

# def main():
#     N = int(input("Enter the level of the carpet: "))
#     carpet = create_carpet(N)
#     print_carpet(carpet)

# if __name__ == "__main__":
#     main()


# N = int(input())

# carpet = ['#']

# for level in range(1, N + 1):
#     prev_carpet = carpet
#     size = len(prev_carpet)
#     new_size = size * 3
#     carpet = [['.' for _ in range(new_size)] for _ in range(new_size)]
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for x in range(size):
#                 for y in range(size):
#                     carpet[i * size + x][j * size + y] = prev_carpet[x][y]

#     carpet = [''.join(row) for row in carpet]

# for row in carpet:
#     print(row)


# N=input()
# Vn=int( N * int(N))
# print(Vn % 998244353)


# MOD = 998244353
# N = int(input())
# d = len(str(N))
# ten_d_mod = pow(10, d, MOD)
# if ten_d_mod == 1:
#     geom_sum = N % MOD
# else:
#     geom_sum = (pow(ten_d_mod, N, MOD) - 1) * pow(ten_d_mod - 1, MOD-2, MOD) % MOD
# V_N_mod = N * geom_sum % MOD
# print(V_N_mod)


# A,B,C = map(int, input().split())

# print(( B + ( A % B ) ) // C)

# N=int(input())
# tmp = list(input().split())
# n=int(input())

# A=[]
# B=[]

# for i in range(n):
#     l=int(input())


# # 入力の読み込み
# N = int(input())

# # テンプレート行の読み込み
# templates = list(input().split())

# # 次の行
# n = int(input())

# # 各変換情報を格納するリスト
# substitutions = []

# for _ in range(n):
#     l = int(input().strip())
    
#     sub_dict = {}
#     for _ in range(l):
#         A, B = input().strip().split()
#         sub_dict[A] = B
    
#     substitutions.append(sub_dict)


# # テンプレートごとに各置換を適用
# results = []
# for template in templates:
#     for sub_dict in substitutions:
#         result = template
#         for key, value in sub_dict.items():
#             result = result.replace(key, value)
#         results.append(result)

# print(results)
# 結果を出力
# for result in results:
    # print(result)



# N = int(input())

# templates = list(input().split())

# n = int(input())

# substitutions = []

# for _ in range(n):
#     l = int(input().strip())
    
#     sub_dict = {}
#     for _ in range(l):
#         A, B = input().strip().split()
#         sub_dict[A] = B
    
#     substitutions.append(sub_dict)

# results = []
# res = []

# # 置換情報があるときはこれ
# for sub_dict in substitutions:
#     for template in templates:
#         result = template
#         substituted = False
#         for key, value in sub_dict.items():
#             if key in result:
#                 result = result.replace(key, value)
#                 substituted = True
#         res.append(result)
#     if substituted:
#         results.append(res)
#         res=[]
#     else:
#         results.append(['Error:','Lack of data'])


# for i in results:
#     print(*i)




# S,T=input().split()

# if S == "AtCoder" and T == "Land":
#     print("Yes")
# else:
#     print("No")


# 0 2 10
# 4 2 10
# 4 8(2+4+(4-2)) 10
# 4 8 10+4+(10-8)=1

# N,A = map(int, input().split()) 

# T = list(map(int, input().split()))

# T[0] += A

# for i in range(1,len(T)):
#     if T[i] < T[i-1]:
#         T[i] += (A + (T[i-1]-T[i]))
#     else:
#         T[i] += A

# for i in T:
#     print(i)





# N,M = map(int, input().split()) #Nこのポップコーン,M種類の味
# S = [input() for _ in range(N)]　#まるなら売り場i味jが残ってる,罰なら売っていない
# print(S)   # 出力を確認 


# N, M = map(int, input().split())
# S = [input() for _ in range(N)]

# masks = []
# for shop in S:
#     mask = 0
#     for j in range(M):
#         if shop[j] == 'o':
#             mask |= (1 << j)
#     masks.append(mask)

# flavors = (1 << M) - 1


# dp = [float('inf')] * (1 << M)
# dp[0] = 0

# for current_mask in range(1 << M):
#     for shop_mask in masks:
#         new_mask = current_mask | shop_mask
#         dp[new_mask] = min(dp[new_mask], dp[current_mask] + 1)

# print(dp[flavors])





# def can_satisfy_requirements(N, A, M, B):
#     boxes = sorted([(A[i], i+1, A[i]) for i in range(N)], key=lambda x: x[2])
#     B_sorted = sorted([(B[i], i+1) for i in range(M)], key=lambda x: x[0])

#     total_cost = 0
#     used_boxes = set()

#     for b, person in B_sorted:
#         found = False
#         for price, box_num, cookies in boxes:
#             if box_num in used_boxes:
#                 continue
#             if cookies >= b:
#                 total_cost += price
#                 used_boxes.add(box_num)
#                 found = True
#                 break
#         if not found:
#             return -1

#     return total_cost


def min_cost_for_requests(N, A, M, B):
    
    boxes = [(A[i], i+1, A[i]) for i in range(N)]
    boxes.sort(key=lambda x: x[2]) 
    
    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0 
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            price, box_num, cookies = boxes[i - 1]
            if cookies >= B[j - 1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + price)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    if dp[N][M] == float('inf'):
        return -1
    
    return dp[N][M]


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = min_cost_for_requests(N, A, M, B)
print(result)







