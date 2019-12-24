from sympy import Symbol, solve
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 



print("------------------------------6번------------------------------")
print("미지수가 x,y,z인 일차방정식인지 판별하고 이유를 설명하라.")
print('Cos(3)x -4y +z = 3^(1/2)\n')
print(' ∴ 일차방정식이다.\n미지수 x,y,z에 곱해진 값은 모두 상수이고 미지수 x,y,z의 지수는 모두 1이기 때문이다. ')

print("------------------------------14번------------------------------")
print('다음 방정식의 해 집합을 구하라.')
print('4x1 + 3x2 + 2x3 = 1')

x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
e1 =  4*x1 +3*x2 +2*x3 - 1

print(' ∴ ' + str(solve([e1])))
print('\n ∴ [x1, x2, x3] = [- 3*t/4 - s/2 + 1/4, s ,t]')



print("------------------------------18번------------------------------")
print("함수의 그래프를 그리고 어떤 해를 갖는지 판정한 후  대수적으로 확인하라.\n")
x = Symbol('x')
y = Symbol('y')
e1 =  0.1*x -0.05*y - 0.2
e2 = -0.06*x + 0.03*y + 0.12
print(solve([e1,e2]))
print("두 방정식은 동일한 그래프이므로 모든 x,y에 대해 같은 해를 갖는다.")
print("[x,y] = [0.5t + 2, t]")
print(" ∴ 해가 무수히 많다.")

x = np.arange(-20,20,0.1)
plt.plot(x,2*x-4,'b')
plt.axis([-4,4,-4,4]) # 범위
plt.xlabel('x Value')
plt.ylabel('y Value')
plt.grid(True)
plt.show()


print("------------------------------22번------------------------------")
print("후진 대입법으로 방정식을 풀어라.")
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
e1 = x1 + 2*x2 + 3*x3
e2 = -5*x2 + 2*x3 
e3 = 4*x3
print(e1)
print('    '+str(e2))
print('            '+str(e3))
print()
print(" ∴  " + str(solve([e1,e2,e3])))



print("\n------------------------------32번------------------------------")
print("주어진 행렬을 첨가계수 행렬로 가지는 연립일차방정식을 구하라.")
x = ['x1','x2','x3','x4','x5']
matrix = [[1,-1,0,3,1,'|2'],[1,1,2,1,-1,'|4'],[0,1,0,2,2,'|0']]
for i in range(len(matrix)) :
    print( '%25s' % matrix[i])
    print()

for i in range(len(matrix)) :
    matrix[i] = list(map(str,matrix[i]))
    for j in range(len(matrix[i])-1) :
        if matrix[i][j] == '1' :
            matrix[i][j] = x[j]
        elif matrix[i][j] == '-1' :
            matrix[i][j] = '-' + x[j]
        elif matrix[i][j] == '0' :
            matrix[i][j] = ''
        else :
            matrix[i][j] = matrix[i][j] + x[j]
            
checkEmpty  = 0
for i in range(len(matrix)) :
    for j in range(len(matrix[i])-1):
        if str(matrix[i][j]) == '' :
            checkEmpty  = checkEmpty + 1
        elif j != 0 and j != checkEmpty and str(matrix[i][j]).count('-') == 0 and matrix[i][j] != '' :
            matrix[i][j] = "+" + matrix[i][j]
            checkEmpty = 0
        
print(" ∴")
for i in range(len(matrix)) :
    print('%20s'% ''.join(matrix[i]).replace('|','='))
        
