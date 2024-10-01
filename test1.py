N=int(input())
num_list = list(map(int, input().split()))
count = len(num_list)
Alice=0
Bob=0
while count != 0:
    Alice += max(num_list)
    num_list.remove(max(num_list))
    if len(num_list) != 0:
        Bob += max(num_list)
        num_list.remove(max(num_list))
    if count < 2:
        count -= 1
    else:
        count -= 2

print(Alice-Bob)