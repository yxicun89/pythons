# S=input()
# if S == "RMS" or S == "RSM" or S == "SRM":
#     print("Yes")
# else:
#     print("No")




def check_substring_match(S, T):
    len_s = len(S)
    len_t = len(T)
    
    for w in range(1, len_s):
        for c in range(1, w + 1):
            constructed_string = ''
            index = c - 1
            
            while index < len_s:
                constructed_string += S[index]
                index += w
                if len(constructed_string) > len_t:
                    break
            
            if constructed_string == T:
                return "Yes"
    
    return "No"

S,T = input().split()
result = check_substring_match(S, T)
print(result) 


# def min_cost_to_rearrange(N, A, W):
#     # 箱の使用状況を確認するためのフラグ
#     visited = [False] * N
#     total_cost = 0
    
#     for i in range(N):
#         if not visited[i]:
#             current = i
#             cycle = []
#             cycle_weight = []
            
#             while not visited[current]:
#                 visited[current] = True
#                 cycle.append(current)
#                 cycle_weight.append(W[current])
#                 current = A[current] - 1
            
#             if len(cycle) > 1:
#                 cycle_sum = sum(cycle_weight)
#                 min_weight = min(cycle_weight)
#                 total_cost += cycle_sum + (len(cycle) - 2) * min_weight
    
#     return total_cost


# N = int(input())
# A = list(map(int, input().split()))
# W = list(map(int, input().split()))

# # 出力
# print(min_cost_to_rearrange(N, A, W))  # 6

