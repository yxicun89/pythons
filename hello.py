print("Hello world!")
x=4
y=3
print(x+y)
strl="レイダーガンダムは5500円だ！"
print(strl)
#print(strl+6464)
listed = [1,2,'a'*4,'b',"abc"*2,"deh"]
print(listed)
def if_test(num):
    if num%2==0:
        print('even')
    else:
        print('odd')
if_test(21)
for i in range(5):
    print(i)
for i in range(2,5):
    print(i)

int1=153
float1=49.3
str1 = "花子さんの身長は{}cm体重は{}kgです。".format(int1,float1)
print(str1)
str2 = "花子さんの身長は{height}cm体重は{weight}kgです。".format(height=int1, weight=float1)
print(str2)
list1 = ["ゆーや","りさ","太郎","ひろと"]
list1.append("二郎")
print(list1[4])
two=[2*i for i in range(5)]
for i in range(4):
    print(two[i])
dict1 = {"次郎":2,"三郎":3,"四郎":4}
print(dict1)
print(dict1["次郎"])
A = {1,2,5}
B = {3,4,5}
C = A | B
print(C)
D=A&B
print(D)
colors = ["red", "blue", "green", "yellow"]

for num, color in zip(range(1, 5), colors):
    print(num, color)
colors = ["red", "blue", "green", "yellow"]

for i, color in enumerate(colors):
    print(i, color)
x = list('Python') 
print(x)
print(list(range(1, 25, 5)))
#リスト型の要素数の所得
l = [0, 1, 2]
print(len(l))

#タプル型の要素数の取得
t = (0, 1, 2,3)
print(len(t))

#文字列型の文字数を取得
s = 'abcde'
print(len(s))
X = [0, 2, 4, 6]

for i in range(len(X)):
        print(i)
print(max([1, 3, 5, 1.5, 10.0]))
print('abcde', end='===')
print('12345')
print(123, 'abc', 999, sep='===')
l = [1, 2, 'str']
print(*l)
l = [1, 2, 'str']
print(*l, sep='-')
x = input()
# 実行すると入力画面が出てくるので、abcと入力

print(x)
# abc

#print(type(x))
#<class 'str'>

