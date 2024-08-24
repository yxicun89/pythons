#２進数のプログラム(10桁統一)
N=int(input())
num_digit=''
while N != 0:
  num_digit+=str(N%2)
  N=int(N/2)
while len(num_digit) < 10:
    num_digit+='0'
if len(num_digit) == 0:
    result=0
else:
    result=num_digit[::-1]
print(result)