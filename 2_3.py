from sympy import Symbol, solve
from sympy.plotting import plot,plot3d
import matplotlib.pyplot as plt
import numpy as np 

print("------------------------------6번------------------------------")
print('벡터 v가 나머지 벡터들의 일차결합인가를 결정하라.')
u1 = [1.0,0.4,4.8]
u2 = [3.4,1.4,-6.4]
u3 = [-1.2,0.2,-1.0]
v = [3.2,2.0,-2.6]

print(" v = ",v)
print(" u1 = ",u1)
print(" u2 = ",u2)
print(" u3 = ",u3)

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
e1 = 1.0*x + 3.4*y -1.2*z -3.2
e2 = 0.4*x + 1.4*y + 0.2*z -2.0
e3 = 4.8*x + -6.4*y -1.0*z +2.6
print()
print(' ∴ ' + str(solve([e1,e2,e3])))
print(' ∴ u1,u2,u3를 통해 v 벡터를 표현할 수 있으므로 일차결합이다.' )


print("------------------------------30번------------------------------")
print('벡터 v가 나머지 벡터들의 일차결합인가를 결정하라.')

v1 = [0,0,0,1]
v2 = [0,0,2,1]
v3 = [0,3,2,1]
v4 = [4,3,2,1]

print(" v1 = ",v1)
print(" v2 = ",v2)
print(" v3 = ",v3)
print(" v3 = ",v4)

c1 = Symbol('c1')
c2 = Symbol('c2')
c3 = Symbol('c3')
c4 = Symbol('c4')

e1 = 0*c1 + 0*c2 + 0*c3 + 4*c4
e2 = 0*c1 + 0*c2 + 3*c3 + 3*c4
e3 = 0*c1 + 2*c2 + 2*c3 + 2*c4
e4 = 1*c1 + 1*c2 + 1*c3 + 1*c4
print()
print(' ∴ ' + str(solve([e1,e2,e3,e4])))
print(' ∴ c1*v1 + c2*v2 + c3*v3 + c4*v4 = 0을 만족하는 스칼라 c의 집합이 모두 0이므로 \n   일차종속 정의에 의해 벡터 집합은 일차독립이다. ')