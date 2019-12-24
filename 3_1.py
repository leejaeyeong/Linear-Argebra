from sympy import Symbol, solve
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------20번------------------------------")
print("행렬의 곱을 이용하여 각 제품을 배달하는 데 소요되는 총 비용을 구하라. ")

C = np.array([[0.75, 0.75, 0.75],
              [1.00, 1.00 ,1.00]])

A = np.array([[200,  75 ],
              [150 , 100],
              [100 , 125]])
print(np.dot(C,A))
print('\n ∴ 창고1로 부터 배달하는데 드는 총 비용은 337.5\n   창고2로 부터 배달하는데 드는 총 비용은 300이다.')


print("------------------------------36번------------------------------")
print("B가 다음과 같다고 하자 B^2015을 구하고, 그 이유를 말하라.")
B = np.array([[1/math.sqrt(2),-1/math.sqrt(2)],
              [1/math.sqrt(2), 1/math.sqrt(2)]])

I = np.array([[1,0],
             [0,1]])

power = 1

while True :
     power = power * 2
     B = np.dot(B,B)
     if np.allclose(I,B) :
          break

B = np.array([[1/math.sqrt(2),-1/math.sqrt(2)],
              [1/math.sqrt(2), 1/math.sqrt(2)]])
C = np.array([[1/math.sqrt(2),-1/math.sqrt(2)],
              [1/math.sqrt(2), 1/math.sqrt(2)]])

power = 2015 % power 

for i in range(1,power) :
     C = np.dot(C,B)
print(C)
print('\n ∴ B의 거듭제곱을 계산하면 B^8이 단위행렬 I가 나온다. B의 2015제곱을 계산할 동안 결과는 8번을 주기로 반복된다.')
print('따라서 2015를 8로 나눈 나머지 수만큼만 B의 행렬곱을 계산해주면 된다.')

print("------------------------------40번------------------------------")
mat = [[0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0]]

print('주어진 조건을 만족하는 6x6 행렬을 구하라.')
print(' \n(a) i<=j 일때 i+j  / i < j 일때 0인 행렬\n')

for i in range(len(mat)) :
     for j in range(len(mat[i])) :
          if j >= i :
               mat[i][j] = i+1 + j+1
          elif i > j :
               mat[i][j] = 0
for i in mat :
     print(i)

print(' \n(b) |i-j| <= 1 일때 1  / |i-j| > 1 일때 0인 행렬\n')

for i in range(len(mat)) :
     for j in range(len(mat[i])) :
          if abs(i-j) <= 1 :
               mat[i][j] = 1
          elif abs(i-j) > 1 :
               mat[i][j] = 0
for i in mat :
     print(i)

print(' \n(c) 6 <= i+j <= 8 일때 1  / 그 외에 경우에 0인 행렬\n')

for i in range(len(mat)) :
     for j in range(len(mat[i])) :
          if i+j >= 6 and i+j <=8 :
               mat[i][j] = 1
          else :
               mat[i][j] = 0
for i in mat :
     print(i)



