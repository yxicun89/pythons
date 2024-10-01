N,A,B=(int(x) for x in input().split())
total=0 #この変数名をsumにするとsum関数使えなくなるから注意（関数名と変数名が同じって言うエラー）
for i in range(N+1):
    result = sum(list(map(int, str(i))))
    if A <= result and B >= result:
        total+=i
print(total)

#各桁を求める関数
#int findSumOfDigits(int n) {
#  int sum = 0;
#  while (n > 0) { // n が 0 になるまで
#    sum += n % 10;
#    n /= 10;
#  }
#  return sum;
#}