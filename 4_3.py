from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------34번------------------------------")
print('A에 대하여 케일리-해밀턴 정리를 증명하라.')

A = np.array([[ 1,1,0],
              [ 1,0,1],
              [ 0,1,1]])

print('cA(λ) = det(A-λI) = -λ^3 + 2λ^2 -2')

print('\nA^2=')
A_2 = np.dot(A,A)
print(A_2)

print('\nA^3=')
A_3 = np.dot(A_2,A)
print(A_3)

print('\n케일리-해밀턴 정리에 의해 cA(λ)가 행렬 A의 특성다항식이면 cA(λ) = 0이다.')
print('cA(A) = -A^3 + 2A^2 + A - 2I이고\n')

print(- A_3 + 2*A_2 + A - 2*np.eye(3))
print('\n ∴ cA(A) = 0 이므로 행렬 A에 대해 케일리-해밀턴 정리가 성립한다.')