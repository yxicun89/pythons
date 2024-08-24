str_list = [input() for _ in range(4)]
count=0
for i in range(4):
    for j in range(4):
        if i!=j and str_list[i]==str_list[j]:
            count+=1
if count!=0:
    print("No")
else:
    print("Yes")

# if "H" in S:
#     S.remove("H")
# if "2B" in S:
#     S.remove("2B")
# if "3B" in S:
#     S.remove("3B")
# if "HR" in S:
#     S.remove("HR")

# if len(S) == 0:
#     print("Yes")
# else:
#     print("No")