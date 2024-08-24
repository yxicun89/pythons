import re

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

str1 = input()
list1 = re.split('[:\s]', str1)
intlist=[int(s) for s in list1 if is_int(s)]
n=len(intlist)
m=intlist[n-1]
newintlist=sorted(intlist[:n-2])+intlist[n-1]
print(newintlist)
strlist=[str(s) for s in list1 if not s.isdecimal()]
string=''
for i in range(n-1):
    if m % intlist[i] == 0:
        string+=strlist[i]
if len(string)==0:
    string+=str(m)
print(string)