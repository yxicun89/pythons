# list = [1,2,1,3,1,3,3,3,3,3]
# maxindex = [i for i, x in enumerate(list) if x == max(list)]

# print(indexes) 

# nums = [1, 5, 2, 1, 4, 5, 1]
 
#     dup = {x for x in nums if nums.count(x) > 1}
#     print(dup)  # {1, 5}
ans=[]
list=["A001","A005","A003","A0010","A00234"]
for i in list:
    ans.append(int(i[3:]))
print(sorted(ans))
# map()
