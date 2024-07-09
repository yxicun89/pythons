N = int(input())
d = len(str(N))

MOD = 998244353

ten_d_mod = pow(10, d, MOD)

# 等比数列の和 (1 + 10^d + 10^(2d) + ... + 10^((N-1)d)) を求める
if ten_d_mod == 1:
    geom_sum = N % MOD
else:
    geom_sum = (pow(ten_d_mod, N, MOD) - 1) * pow(ten_d_mod - 1, MOD-2, MOD) % MOD

V_N_mod = N * geom_sum % MOD

print(V_N_mod)