# r=int(input())

# if r // 100 == 0:
#     print(100 - r)
# elif r // 100 == 1:
#     print(200 - r)
# elif r // 100 == 2:
#     print(300 - r)


# N,T,P = map(int,input().split())

# L=list(map(int,input().split()))

# L.sort()
# if T-L[-P] >= 0:
#     print(T-L[-P])
# else:
#     print(0)

# from itertools import permutations

# def calc_next(S):
#     n = len(S)
#     res = [[n] * 26 for _ in range(n + 1)]
#     for i in range(n - 1, -1, -1):
#         for j in range(26):
#             res[i][j] = res[i + 1][j]
#         res[i][ord(S[i]) - ord('a')] = i
#     return res

# def is_palindrome(s):
#     return s == s[::-1]

# def count_permutations_without_palindromes(S, K):
    
#     n = len(S)
#     unique_permutations = set(permutations(S))
#     print(unique_permutations)

#     count = 0
#     for perm in unique_permutations:
#         perm_str = ''.join(perm)
#         has_palindrome = False
#         for i in range(n - K + 1):
#             if is_palindrome(perm_str[i:i + K]):
#                 has_palindrome = True
#                 break
#         if not has_palindrome:
#             count += 1
    
#     return count

# def main():
#     n, k = map(int, input().split())
#     s = input().strip()
    
#     result = count_permutations_without_palindromes(s, k)
#     print(result)

# if __name__ == "__main__":
#     main()


# from itertools import permutations

# def calc_next(S):
#     n = len(S)
#     res = [[n] * 26 for _ in range(n + 1)]
#     for i in range(n - 1, -1, -1):
#         for j in range(26):
#             res[i][j] = res[i + 1][j]
#         res[i][ord(S[i]) - ord('a')] = i
#     return res

# def is_pal(s):
#     return s == s[::-1]

# def count_perms(S, K):
#     perms = set(permutations(S))
    
#     count = 0
#     for perm in perms:
#         perm_str = ''.join(perm)
#         has_pal = False
#         for i in range(len(S) - K + 1):
#             if is_pal(perm_str[i:i + K]):
#                 has_pal = True
#                 break
#         if not has_pal:
#             count += 1
    
#     return count

# def main():
#     n, k = map(int, input().split())
#     s = input().strip()
    
#     result = count_perms(s, k)
#     print(result)

# if __name__ == "__main__":
#     main()



# def calc_next(S):
#     n = len(S)
#     res = [[n] * 26 for _ in range(n + 1)]
#     for i in range(n - 1, -1, -1):
#         for j in range(26):
#             res[i][j] = res[i + 1][j]
#         res[i][ord(S[i]) - ord('a')] = i
#     return res

# def is_pal(s):
#     return s == s[::-1]

# def count_perms(S, K):
#     n = len(S)
#     next_pos = calc_next(S)
    
#     dp = [0] * (n + 1)
#     dp[0] = 1 

#     for i in range(n):
#         for j in range(26):
#             next_index = next_pos[i][j]
#             if next_index < n:
#                 dp[next_index + 1] += dp[i]

#     total_valid_strings = sum(dp)
    
#     invalid_count = 0
    
#     for i in range(n - K + 1):
#         if is_pal(S[i:i + K]):
#             invalid_count += dp[i]
    
#     return total_valid_strings - invalid_count

# def main():
#     n, k = map(int, input().split())
#     s = input().strip()
    
#     result = count_perms(s, k)
#     print(result)

# if __name__ == "__main__":
#     main()

# def calc_next(S):
#     n = len(S)
#     res = [[n] * 26 for _ in range(n + 1)]
#     for i in range(n - 1, -1, -1):
#         for j in range(26):
#             res[i][j] = res[i + 1][j]
#         res[i][ord(S[i]) - ord('a')] = i
#     return res

# def add(a, b):
#     return a + b

# def count_perms(S, K):
#     n = len(S)
#     T = S[::-1]  # Reverse of S

#     ns = calc_next(S)
#     nt = calc_next(T)

#     dp = [[0] * (n + 1) for _ in range(n + 1)]
#     dp[0][0] = 1

#     for i in range(n):
#         for j in range(n):
#             for k in range(26):
#                 ni = ns[i][k]
#                 nj = nt[j][k]
#                 if ni + nj + 2 > n:
#                     continue
#                 dp[ni + 1][nj + 1] = add(dp[ni + 1][nj + 1], dp[i][j])

#     res = 0
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if i + j <= n:
#                 num = 0
#                 for k in range(26):
#                     if ns[i][k] + 1 + j <= n:
#                         num += 1
#                 res = add(res, dp[i][j] * num)

#     return res - 1

# def main():
#     n, k = map(int, input().split())
#     s = input().strip()
    
#     result = count_perms(s, k)
#     print(result)

# if __name__ == "__main__":
#     main()


# def nth_palindrome_number(n):
#     if n <= 0:
#         return -1 
    
#     palindromes = []
#     num = 0
    
#     while len(palindromes) < n:
#         if str(num) == str(num)[::-1]:
#             palindromes.append(num)
#         num += 1
    
#     return palindromes[-1]

# n = int(input())
# result = nth_palindrome_number(n)
# print(result)


def generate_palindrome(base):
    s = str(base)
    return int(s + s[::-1])

def generate_palindrome_odd(base):
    s = str(base)
    return int(s + s[-2::-1])

def nth_palindrome_number(n):
    if n <= 0:
        return -1
    
    count = 0
    length = 1
    
    while True:
        start = 10 ** ((length - 1) // 2)
        end = 10 ** (length // 2)
        for i in range(start, end):
            count += 1
            if count == n:
                return generate_palindrome(i)
        
        start = 10 ** (length // 2)
        end = 10 ** ((length + 1) // 2)
        for i in range(start, end):
            count += 1
            if count == n:
                return generate_palindrome_odd(i)
        
        length += 1

# テスト
n = int(input())
result = nth_palindrome_number(n)
print(result)


