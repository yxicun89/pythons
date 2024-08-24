def count_final_strings(n, s):
    MOD = 10**9 + 7
    
    count_A = s.count('A')
    count_B = s.count('B')
    
    # 最終的な文字列のパターン数は、AとBの組み合わせ数
    final_count = (count_A + 1) * (count_B + 1) % MOD
    
    return final_count

# 入力
N = int(input())
S = input()

# 結果を計算して表示
result = count_final_strings(N, S)
print(result)
