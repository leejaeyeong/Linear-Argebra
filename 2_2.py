from sympy import Symbol, solve
from sympy.plotting import plot,plot3d
import matplotlib.pyplot as plt
import numpy as np 

print("------------------------------8번------------------------------")
print('행렬이 행사다리꼴인지 아닌지 판정하고, 행사다리꼴이면, 기약 행사다리꼴이 되는지도 말하라.')
matrix = [[2,1,3,5],
          [0,0,1,-1],
          [0,0,0,3],
          [0,0,0,0]]

echelon_form = True

for i in range(len(matrix)) :
    for j in range(i) :
        if matrix[i][j] == 0 and i == 0 and j == 0 :
            echelon_form = False
            break
        elif matrix[i][j] != 0 and i == 0 and j == 0 : 
            break
        else :
            if matrix[i][j] != 0 :
                echelon_form = False
                break

    if not echelon_form : break

zero_bttom = True
row_size = len(matrix)
for i in range(row_size) :
    if matrix[row_size-1][i] != 0 :
        zero_bttom = True
        break

print(' ∴ 행사다리꼴.') if echelon_form and zero_bttom else print(' ∴ 행사다리꼴 아님.')

reduce_form = True
for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        if matrix[i][j] != 0 and matrix[i][j] != 1 :
            reduce_form = False
            break
        elif  matrix[i][j] == 1 :
            break

    if not reduce_form : break

print(' ∴ 기약행사다리꼴.') if reduce_form else print(' ∴ 기약행사다리꼴 아님.')



print("------------------------------34번------------------------------")
print('가우스 소거법 또는 가우스-조르당 소거법을 이용해 풀어라.\n')
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

print('%30s'% 'a + b + c + d = 4')
print('%30s'% 'a + 2b + 3c + 4d = 10')
print('%30s'% 'a + 3b + 6c + 10d = 20')
print('%32s'% 'a + 4b + 10c + 20d = 35\n\n')

mat = [[1, 1, 1, 1, 4],
       [1, 2, 3, 4, 10],
       [1, 3, 6, 10, 20],
       [1, 4, 10, 20 ,35]]

print('첨가 행렬 :')
for x in mat :
    print(x)

ex = row_reduce(mat)

print('행사다리꼴 출력하ㄱ----------------------------------------------')
for i in ex :
    print(i)

print('행사다리꼴 출력하ㄱ----------------------------------------------')

print('\n\n가우스 소거 행렬 :')
for x in mat :
    print(x)

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e1 = ex[0][0]*a + ex[0][1]*b + ex[0][2]*c + ex[0][3]*d - ex[0][4]
e2 = ex[1][0]*a + ex[1][1]*b + ex[1][2]*c + ex[1][3]*d - ex[1][4]
e3 = ex[2][0]*a + ex[2][1]*b + ex[2][2]*c + ex[2][3]*d - ex[2][4]
e4 = ex[3][0]*a + ex[3][1]*b + ex[3][2]*c + ex[3][3]*d - ex[3][4]

print('\n ∴')
print('해가 없다.') if len(solve([e1,e2,e3,e4])) == 0 else print(solve([e1,e2,e3,e4]))


print("------------------------------47번------------------------------")
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
print('\n(a) 공통 교선을 가지는 세 평면의 예를 들어라.)')
plot3d(x,8*x,16*x,(x,-5,5),(y,-5,5),(z,-5,5))
print('\n(b) 두 평면들은 교차하고 세 평면의 공통 교선이 없는 세 평면의 예를 들어라.')
plot3d(x,5*x-20,-x,(x,-5,5),(y,-5,5),(z,-5,5))
print('\n(c) 두 평면만 평행한 세 평면의 예를 들어라.')
plot3d(x,x+5,-x,(x,-5,5),(y,-5,5),(z,-5,5))
print('\n(d) 한 점에서만 교차하는 세 평면의 예를 들어라.')
plot3d(x-y,y-x,5*(x-y),(x,-5,5),(y,-5,5),(z,-5,5))

