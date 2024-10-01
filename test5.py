N,K = map(int, input().split())
total = 0
for i in range(N+1):
    if str(i).count(f"{K}"):
        total += i
print(total)