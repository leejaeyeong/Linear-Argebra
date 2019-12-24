from sympy import *
from sympy.plotting import plot
import numpy as np 
import math

print("------------------------------21번------------------------------")
print('주어진 고윳값과 이에 대응하는 고유 벡터를 갖는 2x2대칭 해렬을 구하라.')
print('λ1 = -1, λ2 = 2, v1 = [1,1] , v2 = [1,-1]')

v1 = np.array([1,1])
v2 = np.array([1,-1])
print('\nv1과 v2는 이미 직교이므로 정규화하면 행렬 Q는')
q1 =  v1*(1/np.linalg.norm(v1))
q2 =  v2*(1/np.linalg.norm(v2))

Q = []
Q.append(q1)
Q.append(q2)

def transpose(mat) :
    tr = [[0]*2,
          [0]*2]
    for i in range(len(mat)) :
        for j in range(len(mat[i])) :
            tr[j][i] = mat[i][j]
    return tr

Q = transpose(Q)

for i in Q :
    print(i)

print('\n ∴ λ1과 λ2에 대응하는 v1,v2를 갖는 2x2 대칭 행렬은')

D = np.array([[-1,0],
              [0,2]])
print(np.dot(np.dot(Q,D),transpose(Q)))

print("------------------------------23번------------------------------")
print('주어진 고윳값과 이에 대응하는 고유 벡터를 갖는 3x3대칭 해렬을 구하라.')
print('λ1 = 1, λ2 = 2, λ3 = 3, v1 = [1,1,0] , v2 = [1,-1,1], v3 = [-1,1,2]')


v1 = np.array([1,1,0])
v2 = np.array([1,-1,1])
v3 = np.array([-1,1,2])

print('\nv1과 v2, v3는 이미 직교이므로 정규화하면 행렬 Q는')
q1 = v1*(1/np.linalg.norm(v1))
q2 = v2*(1/np.linalg.norm(v2))
q3 = v3*(1/np.linalg.norm(v3))

Q = []
Q.append(q1)
Q.append(q2)
Q.append(q3)

def transpose(mat) :
    tr = [[0]*3,
          [0]*3,
          [0]*3]
    for i in range(len(mat)) :
        for j in range(len(mat[i])) :
            tr[j][i] = mat[i][j]
    return tr

Q = transpose(Q)

for i in Q :
    print(i)

print('\n ∴ λ1과 λ2, λ3 에 대응하는 v1,v2,v3를 갖는 3x3 대칭 행렬은')

D = np.array([[1,0,0],
              [0,2,0],
              [0,0,3]])
              
print(np.dot(np.dot(Q,D),transpose(Q)))