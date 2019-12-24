from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------6번------------------------------")
print('주어진 v가 행렬 A의 고유벡터임을 보이고, 대응하는 고윳값을 구하라.')


A = np.array([[ 0,1,-1],
              [ 1,1, 1],
              [ 1,2, 0]])

v = np.array([[-2],
              [1],
              [1]])
print('두 벡터 Av의 결과는')
print(np.dot(A,v))
print('이므로 0*v로 표현할 수 있다. \n  ∴ 따라서 v는 고유값 0을 갖는 A의 고유 벡터이다.')

print("------------------------------12번------------------------------")
print('다음에 주어진 λ의 값이 행렬 A의 고윳값임을 보이고, 이 고윳값에 대응하는 고유벡터를 구하라.')
print('Av = 2v  ---> (A-2I)v = 0')
A = np.array([[ 3,1,-1],
              [ 1,1, 1],
              [ 4,2, 0]])

I = np.array([[ 1,0,0],
              [ 0,1,0],
              [ 0,0,1]])

R = A - 2*I
print(R)

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
e1 = 1*x + 1*y - 1*z 
e2 = 1*x - 1*y + 1*z 
e3 = 4*x + 2*y - 2*z 

print('\n (A-2I) 행렬의 해는 다음과 같다.')
print(' ∴ ' + str(solve([e1,e2,e3])))
print('  ∴ 따라서 x=0 이고 y = z인 경우, λ=2는 행렬 A의 고윳값이다.')

