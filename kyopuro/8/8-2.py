from collections import deque

Q=int(input())
query=[input().split() for i in range(Q)]

S=deque()
for q in query:
  if q[0] == "1":
    S.append(q[1])
  if q[0] == "2":
    print(S[0])
  if q[0] == "3":
    S.popleft()