from sympy import *
from sympy.plotting import plot
import numpy as np 
import math

print("------------------------------6번------------------------------")
print('그램-슈미트 과정을 적용하여 W의 직교기저를 구하여라.')

x1 = np.array([2,-1,1,2])
x2 = np.array([3,-1,0,4])
x3 = np.array([1,1,1,1])

v2 = x2 - (np.dot(x1,x2) / np.dot(x1,x1))*x1
v3 = x3 - (np.dot(x1,x3) / np.dot(x1,x1))*x1 - (np.dot(v2,x3) / np.dot(v2,v2))*v2

print('\n ∴ 직교기저는  ')
print('v1 = ', x1)
print('v2 = ', v2)
print('v3 = ', v3)

print("------------------------------8번------------------------------")
print('부분공간 W에 대한 v의 직교분해를 구하여라.')
v = np.array([1,4,0,2])

v1_v = (np.dot(x1,v) / np.dot(x1,x1))*x1
print('proj_v1_(v) = ', v1_v)
v2_v = (np.dot(v2,v) / np.dot(v2,v2))*v2
print('proj_v2_(v) = ', v2_v)
v3_v = (np.dot(v3,v) / np.dot(v3,v3))*v3
print('proj_v3_(v) = ', v3_v)

print('\n ∴ v1,v2,v3와 직교하는 v는')
print(v - v1_v - v2_v - v3_v)


print("------------------------------9번------------------------------")
print('다음에 주어진 행렬의 열공간에 대한 직교기저를 그램-슈미트 과정으로 구하라.')
A = [[0,1,1],
    [1,0,1],
    [1,1,0]]

for i in A :
    print(i)

print('\nA에 대해 기본행연산을 수행하면')

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

A = mat_subtraction(convert_front_one(row_reduce(A)))

for i in A :
    print(i)

print('\n따라서 주어진 행렬은 열 공간에 대해 선형적으로 독립인것을 알 수 있다. ')
print('주어진 행렬의 각 열을 x1,x2,x3로 정한다.')

x1 = np.array([0,1,1])
x2 = np.array([1,0,1])
x3 = np.array([1,1,0])

v1 = x1
v2 = x2 - (np.dot(v1,x2)/np.dot(v1,v1))*v1
v3 = x3 - (np.dot(v1,x3)/np.dot(v1,v1))*v1 - (np.dot(v2,x3)/np.dot(v2,v2))*v2 

print('\n ∴ 주어진 행렬의 열공간에 대한 직교기저는')
print('v1 = ', v1)
print('v2 = ', v2)
print('v3 = ', v3)

