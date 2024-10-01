from sys import stdin
input = stdin.readline
N=int(input())
num_list = [int(input()) for _ in range(N)]
#print(num_list)
#print(set(num_list))
print(len(set(num_list)))