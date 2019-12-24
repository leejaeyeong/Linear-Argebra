from sympy import Symbol, solve
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------6번------------------------------")
print("정리 3.8을 이용하여 다음 행렬의 역행렬을 구하라.")
B = np.array([[1/math.sqrt(2),1/math.sqrt(2)],
              [-1/math.sqrt(2), 1/math.sqrt(2)]])
print(np.linalg.inv(B))

print("------------------------------12번------------------------------")
print("정리 3.25의 방법을 이용하여 다음 연립방정식의 해를 구하여라.")
print('                    x1 - x2 = 1')
print('                   2x1 + x2 = 2')

# 연립 방정식을 첨가 계수 행렬로 표현
A = np.array([[1,-1],
              [2, 1]])
answer = np.array([[1],
                   [2]])
print(' ∴ 연립방정식의 해는')
# A의 역행렬을 우변에 행렬에 곱함
print(np.linalg.inv(A).dot(answer))



C = np.array([[0,1,0,1],
              [0,0,0,1],
              [1,0,0,0],
              [1.0,1,0]])

A = np.array([[0,1,0,1],
              [0,0,0,1],
              [1,0,0,0],
              [1.0,1,0]])
print(np.dot(C,A))

C = np.array([[0.75, 0.75, 0.75],
              [1.00, 1.00 ,1.00]])

A = np.array([[200,  75 ],
              [150 , 100],
              [100 , 125]])
print(np.dot(C,A))