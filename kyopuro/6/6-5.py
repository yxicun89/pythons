# N=int(input())
# A=list(map(int,input().split()))

# # 個数を数える
# cnt = [ 0 ] * 101
# Answer = 0
# for i in range(N):
# 	cnt[A[i]] += 1

# # 答えを求める
# for i in range(1, 101):
#     # print(cnt[i] * (cnt[i]-1) * (cnt[i]-2) // 6)
# 	Answer += cnt[i] * (cnt[i]-1) * (cnt[i]-2) // 6; #nC3だから6で割ればいい,これnC3の計算を100までやってる
# print(Answer)

class point2d:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
  def dist(self,p):
    return ((self.x-p.x)**2 + (self.y - p.y)**2)**0.5
    
def play_greedy(n,points):
  current_place=0
  visited = [False] * n
  visited[0] = True
  P=[0]
  for i in range(1,n):
    mindist=10**10
    min_id = -1
    for j in range(n):
      if not visited[j] and mindist > points[current_place].dist(points[j]):
        mindist = points[current_place].dist(points[j])
        min_id = j
    
    visited[min_id] = True
    P.append(min_id)
    current_place=min_id
  P.append(0)
  return P
  
N=int(input())
points=[None] * N
for i in range(N):
  x,y=map(int,input().split())
  points[i]=point2d(x,y)
  
answer = play_greedy(N,points)

for i in answer:
  print(i+1)