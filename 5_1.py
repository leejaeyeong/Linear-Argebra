from sympy import *
from sympy.plotting import plot
import numpy as np 
import math

print("------------------------------6번------------------------------")
print('벡터들의 집합이 직교집합인지 판정하라.')

v1 = np.array([1,0,-1,1])
v2 = np.array([-1,0,1,2])
v3 = np.array([1,1,1,0])
v4 = np.array([0,-1,1,1])

print('v1*v2 =',np.dot(v1,v2))
print('v1*v3 =',np.dot(v1,v3))
print('v1*v4 =',np.dot(v1,v4))
print('v2*v3 =',np.dot(v2,v3))
print('v2*v4 =',np.dot(v2,v4))
print('v3*v4 =',np.dot(v3,v4))

print('\n 직교집합에서는 서로 다른 두 벡터는 항상 수직이여야한다.\n ∴ 주어진 벡터집합은 직교집합이 아니다.' )


print("------------------------------10번------------------------------")
print('벡터들이 집교기저가 됨을 보이고 w를 이 기저벡터들의 일차결합으로 나타내라. 또한 w의 좌표벡터를 구하라.')

v1 = np.array([1,1,1])
v2 = np.array([1,-1,0])
v3 = np.array([1,1,-2])
w = np.array([1,2,3])

print('v1*v2 =',np.dot(v1,v2))
print('v1*v3 =',np.dot(v1,v3))
print('v1*v4 =',np.dot(v2,v3))

print('\n ∴  주어진 벡터들은 R^3의 직교기저이다.  ')

def coordinate(param1, param2) :    # 좌표를 구하는 함수
    x = np.dot(param1,param2)
    y = np.dot(param1,param1)
    return x/y

c1 = coordinate(v1,w)
c2 = coordinate(v2,w)
c3 = coordinate(v3,w)

print('\n ∴ w를 이 기저벡터들의 일차결합으로 나타내면 다음과 같다.')
print('     w =',c1,'*v1',c2,'*v2',c3,'*v3')

print('\n ∴ 좌표벡터 [w]B는')
res = np.array([c1,c2,c3])
print('     [w]B=',res)

print("------------------------------14번------------------------------")
print('주어진 직교집합이 정규직교 집합인지 판정하고 정규직교 집합이 아니면 정규직교 집합을 구하라.')

v1 = np.array([1/2, 1/2, -1/2, 1/2])
v2 = np.array([0, 1/3, 2/3, 1/3])
v3 = np.array([1/2, -1/6, 1/6, -1/6])

print('||v1|| = ',np.linalg.norm(v1))
print('||v2|| = ',np.linalg.norm(v2))
print('||v3|| = ',np.linalg.norm(v3))

print('\n∴\n v2,v3가 단위벡터가 아니기 때문에 주어진 집합은 정규직교 집합이 아니다.\n 이를 정규화여 정규직교 집합을 구하면')

v2 = 1/np.linalg.norm(v2)*v2
v3 = 1/np.linalg.norm(v3)*v3

print('∴')
print(v1)
print(v2)
print(v3)

print("------------------------------30번------------------------------")
print('직교행렬이 회전변환을 나타내는지, 대칭변환을 나타내는지 결정하고 회전각 또는 대칭선을 구하라.')

arr = [[-1/2,math.sqrt(3)/2],[-math.sqrt(3)/2,-1/2]]
print('\n ∴ 행령의 det가 ',np.linalg.det(arr),'≈ 1 이므로\n 주어진 행렬은 회전변환을 나타내고 θ는')
print('    cosθ = 1/sqrt(2), sinθ = -sqrt(3)/2를 만족하는 θ = 4pi/3 = 240°')

