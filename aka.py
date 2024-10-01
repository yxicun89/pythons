n,w=(int(x) for x in input().split())  #従業員人数と作業できる回数
#A = [input().split() for i in range(n)]
A=[int(x) for x in input().split()] #作業量、添字が従業員番号
new=[]
count=0
while(len(A)>0):
    for i in range(len(A)):
        if A[0]>w:
            A[0]-=w
            A.append(A[0])
            A.pop(0)
        else:
            print(i+count+1)
            A.pop(0)
    count+=1
