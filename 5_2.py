from sympy import *
from sympy.plotting import plot
import numpy as np 
import math

print("------------------------------8번------------------------------")
print('행공간과 영공간의 기저를 구하고 row(A)의 모든 벡터는 null(A)의 모든 벡터와 수직임을 보여라.')

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
            
            for r in rows_with_nonzero[1:] :
                if r is not pivot:
                    multiplier = mat[r][c] / mat[pivot][c]
                    mat[r] = [a - multiplier*b for a, b in zip(mat[r], mat[pivot])]
    for r in row_idx:
        rref.append(mat[r])
        
    for i in range(len(rref)) :
        for j in range(len(rref[i])) :
            rref[i][j] = int(rref[i][j])

    return rref


def convert_front_one(mat) :
    for i in range(len(mat)) :
        divide = 0
        state = False
        for j in range(len(mat[i])) :
            if state == False :
                if mat[i][j] != 0 and mat[i][j] != 1 :
                    if divide == 0 :
                        divide = mat[i][j]
                        mat[i][j] = int(mat[i][j] / divide)
                        state = True
                elif  mat[i][j] == 1 :
                    break
            else :
                mat[i][j] = int(mat[i][j] / divide) 

    return mat

def mat_subtraction(mat) :
    for i in range(len(mat)-1,0,-1) :
        for j in range(len(mat[i])) :
            if mat[i][j] == 1 :
                for k in range(i-1,-1,-1) :
                    save = mat[k][j]
                    for z in range(j,len(mat[i])) :
                        mat[k][z] = mat[k][z] - save*mat[i][z]
                break
                    
                        
                        
    return mat


A = [[1,1,-1,0,2],
    [-2,0,2,4,4],
    [2,2,-2,0,1],
    [-3,-1,3,4,5]]

B = mat_subtraction(convert_front_one(row_reduce(A)))

print('\n ∴ 행공간의 대한 기저는 ')
for i in range(len(B)-1) :
    print('u{} = '.format(i+1),B[i])

print('\n기약행 사다리꼴에서 x3, x4를 s,t로 표현하면')
print('∴ 영공간의 대한 기저는 ')
print('v1 = [1,0,1,0,0]\nv2 = [2,-2,0,1,0]')

u1 = np.array(B[0])
u2 = np.array(B[1])
u3 = np.array(B[2])

v1 = np.array([1,0,1,0,0])
v2 = np.array([2,-2,0,1,0])

print('\n ∴ row(A)와 null(A)의 모든 벡터와의 수직임을 보인다. ')
print('u1*v1 =',np.dot(u1,v1))
print('u1*v2 =',np.dot(u1,v2))
print('u2*v1 =',np.dot(u2,v1))
print('u2*v2 =',np.dot(u2,v2))
print('u3*v1 =',np.dot(u3,v1))
print('u3*v2 =',np.dot(u3,v2))

print("------------------------------10번------------------------------")
print('8번에 대한 열공간의 기저와 A^T의 영공간의 기저를 구하여라. \n그리고 col(A)의 모든 벡터는 null(A^T)의 모든 벡터와 수직임을 보여라')

print('\n열공간에 대한 기저는 주어진 행렬을 기약행사다리꼴로 바꾸고 선행성분을 갖는 열을 원래의 행렬 A에서 선택하는 것이므로')

u1 = np.array([1,-2,2,-3])
u2 = np.array([1,0,2,-1])
u3 = np.array([2,4,1,5])
print('u1 = ',u1)
print('u2 = ',u2)
print('u3 = ',u3)

def transpose(mat) :
    tr = [[0]*4,
          [0]*4,
          [0]*4,
          [0]*4,
          [0]*4]
    for i in range(len(mat)) :
        for j in range(len(mat[i])) :
            tr[j][i] = mat[i][j]
    return tr

A = [[1,1,-1,0,2],
    [-2,0,2,4,4],
    [2,2,-2,0,1],
    [-3,-1,3,4,5]]

A_T = transpose(A)
print('\n∴ A^T는 ')
for i in A_T :
    print(i)

print('\n∴ A^T의 영공간의 기저는 ')
A_T_null = mat_subtraction(convert_front_one(row_reduce(A_T)))

print('[A^T | 0] = ')

for i in A_T_null :
    print('           ',i)

print('\n x4를 s로 표현하면')
print('∴ 영공간의 대한 기저는 ')
print('v1 = [-1,-1,1,1]')

v1 = np.array([-1,-1,1,1])


print('\n ∴ col(A)와 null(A^T)의 모든 벡터와의 수직임을 보인다. ')
print('u1*v1 =',np.dot(u2,v1))
print('u2*v1 =',np.dot(u2,v1))
print('u3*v1 =',np.dot(u3,v1))


print("------------------------------17번------------------------------")
print('벡터 ui에 의해 생성된 부분공간 W 위로의 v의 정사영을 구하라.')

v = np.array([1,2,3])
u1 = np.array([2,-2,1])
u2 = np.array([-1,1,4])

x1 = np.dot(u1,v) / np.dot(u1,u1)
x2 = np.dot(u2,v) / np.dot(u2,u2)

print('\n ∴\n proj_w(V) = ', x1*u1 + x2*u2)

print("------------------------------22번------------------------------")
print('주어진 W에 대한 v의 직교분해를 구하여라.')

v = np.array([2,-1,5,6])
u1 = np.array([1,1,1,0])
u2 = np.array([1,0,-1,1])

x1 = np.dot(u1,v) / np.dot(u1,u1)
x2 = np.dot(u2,v) / np.dot(u2,u2)

print('\n ∴\n proj_w(V) = ', x1*u1 + x2*u2)

print(' proj_w⊥ (V) = ', v - (x1*u1 + x2*u2))