import numpy as np
import random
import time
import sys

N=100
Q=1000
A=np.array([list(map(int,input().split()) for i in range(N))])

X=[random.randint(0,N-1) for i in range(Q)]
Y=[random.randint(0,N-1) for i in range(Q)]
H=[1]*Q
