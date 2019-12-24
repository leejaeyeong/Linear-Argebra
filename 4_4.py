from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------4번------------------------------")
print('A와 B가 닮은 행렬이 아님을 보여라.')

A = np.array([[ 1,2,0],
              [ 0,1,-1],
              [ 0,-1,1]])

B = np.array([[ 2,1,1],
              [ 0,1,0],
              [ 2,0,1]])

print('cA(λ) = det(A-λI) = -λ^3 + 3λ^2 -2λ')
print('\ncB(λ) = det(B-λI) = -λ^3 + 4λ^2 -3λ')

print('\n두 행렬이 닮음이기 위해서는 특성 다항식이 같아야하므로 \n ∴  두 행렬은 닮음이 아니다.')

print("------------------------------6번------------------------------")
print('행렬 A가 대각화 가능한 행렬일 때 A의 고윳값과 그에 대응하는 고유공간의 기저를 나열하라.')


A = [[1,1,1],
     [0,0,1],
     [1,1,0]]

P = [[3,1,0],
     [1,-1,1],
     [2,0,-1]]

D = [[2,0,0],
     [0,0,0],
     [0,0,-1]]

vector = []

print('\n A에 대한 가역행렬 P와 대각행렬 D가 존재하는 것은 P의 열벡터는 A의 일차독립인 고유벡터이고')
print('D의 대각성분은 같은 순서로 P의 열벡터에 대응하는 A의 고윳값이므로\n\n∴')

for i in range(len(D)) :
    for j in range(len(D)) :
        if i == j :
            print('λ'+str(i+1)+' = '+str(D[i][j])+'의 고유벡터는, ', end='')

            for k in range(len(P)) :
                for z in range(len(P)) :
                    if z == i :
                        vector.append(P[k][z])
                if k == len(P) - 1 :
                    print('span('+str(vector)+'^T)\n')
                    vector = []


print("------------------------------21번------------------------------")
print('주어진 행렬의 2015 거듭제곱을 구하여라.')

A = np.array([[ 1, 1, 1],
              [ 0,-1, 0],
              [ 0, 0,-1]])

I = np.eye(3)

A_plus_I = A + I
A_miner_I = A - I

print('\n[A + I | 0] :')
for i in A_plus_I :
    print('             ',i)

print('\n[A - I | 0] :')
for i in A_miner_I :
    print('             ',i)

print('\n행렬 A에 대한 고유값에 대한 고유벡터로 P를 구하면')

P = np.array([[-1,-1,1],
              [ 0,2, 0],
              [ 2, 0,0]])

P_inv = np.linalg.inv(P) # P의 역행렬 

D = np.dot(np.dot(P_inv,A),P) # D = P^(-1)*A*P


print('∴  A^2015는 P*D^2015*P^(-1)이므로 이를 계산하면')

Cal = np.eye(3)

def power(arr, v) :
    for i in range(v) : # 0 ~ 2014 => 
        arr = np.dot(arr,D)
    return arr

print(np.dot(np.dot(P,power(Cal,2015)),P_inv))
print('\n∴  A^2015는 A이다.(즉, 자기 자신이다.)')