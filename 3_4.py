from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------4번------------------------------")
print('A의 LU 분해를 이용해 방정식 Ax = b의 해를 구하라.')
L =  [[ 1,0,0],
      [3/2,1,0],
      [-1/2, 0,1]]

U =  [[ 2,-4,0],
     [ 0,5,4],
     [0, 0,2]]

y1 = Symbol('y1')
y2 = Symbol('y2')
y3 = Symbol('y3')
e1 = 1*y1 + 0*y2 + 0*y3 - 2 
e2 = (3/2)*y1 + 1*y2 + 0*y3 - 0
e3 = -(1/2)*y1 + 0*y2 + 1*y3 + 5

print('\n (1) Ly = b의 결과')
print(' ∴ ' + str(solve([e1,e2,e3])))

x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
e1 = 2*x1 - 4*x2 + 0*x3 - 2 
e2 = 0*x1 + 5*x2 + 4*x3 + 3
e3 = 0*x1 + 0*x2 + 2*x3 + 4

print('\n (2) Ux = y의 결과')
print(' ∴ ' + str(solve([e1,e2,e3])))

print('\n 따라서 Ax = b의 해는 '+str(solve([e1,e2,e3])))


print("------------------------------8번------------------------------")
print('주어진 행렬의 LU 분해를 구하라.')
# U를 구하기 위한 행사리꼴 변환 함수 
def row_reduce(mat):
    rref = []
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
      
    for c in range(col_idx):
        rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0]
        if rows_with_nonzero:
            pivot = rows_with_nonzero[0]
            row_idx.remove(pivot)
            rref.append(mat[pivot])
            
            for r in rows_with_nonzero[1:]:
                if r is not pivot:
                    multiplier = mat[r][c] / mat[pivot][c]
                    mat[r] = [a - multiplier*b for a, b in zip(mat[r], mat[pivot])]
    for r in row_idx:
        rref.append(mat[r])
        
    for i in range(len(rref)) :
        for j in range(len(rref[i])) :
            rref[i][j] = int(rref[i][j])

    return rref

A = [[2,-4],
     [3, 1]]

U = row_reduce(A)

print('\nU를 구하는 과정에서 R2 - (3/2)R1의 행 연산이 이루어졌으므로 L 행렬의 (2,1)의 요소는 3/2가 된다.')
L = [[ 1 ,0],
     [3/2,1]]

print('\n ∴ 따라서')
print('U = ')
for i in U :
    print('   ',end='')
    print(i)
print('L = ')
for i in L :
    print('   ',end='')
    print(i)

print("------------------------------12번------------------------------")
print('주어진 행렬의 LU 분해를 구하라.\n')
A = [[2,2,2,1],
     [-2,4,-1,2],
     [4,4,7,3],
     [6,9,5,8]]

U = row_reduce(A) # 문제 8번의 row_reduce() 메소드
L = [[1 , 0 , 0 ,  0 ],
     [-1, 1 , 0 ,  0 ],
     [2 , 0,  1 ,  0 ],
     [3 ,1/2 , -1/2 ,1]]

print('상삼각행렬 U를 구하는 과정에서 행 연산')
print('R2-(-R1)')
print('R3-2R1')
print('R4-3R1')
print('R3-0R2')
print('R4-(1/2)R2')
print('R4-(-1/2)R3이 수행되었다.')

print('\n ∴ 따라서')
print('U = ')
for i in U :
    print('   ',end='')
    print(i)
print('L = ')
for i in L :
    print('   ',end='')
    print(i)

print("------------------------------14번------------------------------")
print('U가 행사다리꼴 행렬이 되도록하여 LU분해의 정의를 정사각이 아닌 행렬로 까지 일반화하라.\n')

A = [[1 , 2 , 0 , -1 , 1],
     [-2,-7 , 3 ,  8 ,-2],
     [1 , 1 , 3 ,  5 , 2],
     [0 , 3 ,-3 , -6 , 0]]
    
U = row_reduce(A) # 문제 8번의 row_reduce() 메소드
L = [[1 , 0 , 0 ,  0 ],
     [-2, 1 , 0 ,  0 ],
     [1 ,1/3, 1 ,  0 ],
     [0 ,-1 , 0 ,  1 ]]

print('상삼각행렬 U를 구하는 과정에서 행 연산')
print('R2-(-2R1)')
print('R3-R1')
print('R4-0R1')
print('R3-(1/3)R1')
print('R4-(-1R2)이 수행되었다.')

print('\n ∴ 따라서')
print('U = ')
for i in U :
    print('   ',end='')
    print(i)
print('L = ')
for i in L :
    print('   ',end='')
    print(i)
