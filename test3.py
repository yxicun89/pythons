N,Y=(int(x) for x in input().split())
yukiti = -1
itiyo = -1
hideo = -1
for i in range(N+1):
    for j in range(N+1-i):
        k = N - i - j
        t = 10000 * i + 5000 * j + 1000 * k
        if t == Y:
            yukiti = i
            itiyo = j
            hideo = k

print(f"{yukiti} {itiyo} {hideo}")