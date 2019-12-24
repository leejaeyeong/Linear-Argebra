from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np 
import math

print("------------------------------10번------------------------------")
print('적합한 행과 열에 대해 여인수 전개식을 사용하여 행렬식을 구하라.')


A = np.array([[ 'cosθ','sinθ','tanθ'],
              [ '0','cosθ', '-sinθ'],
              [ '0','sinθ', 'cosθ']])
print(A)
print('\n ∴ 1열에 대한 여인수 전개를 구하면 0의 값은 결국 0이므로 행렬식은 ')

print('cosθ(cosθ · cosθ − (− sinθ) · sinθ) = cosθ(cos^2θ + sin^2θ) = cosθ')





print("------------------------------14번------------------------------")
print('적합한 행과 열에 대해 여인수 전개식을 사용하여 행렬식을 구하라.')
def twobytwo_det(arr) :
    e1, e2 = 0,0
    if len(arr) == 2 :
        for i in range(len(arr)) :
            for j in range(len(arr)) :
                if i == 0 and j == 0 :
                    e1 = arr[i][j]
                elif i == 0 and j == 1 :
                    e2 = arr[i][j]
                elif i == 1 and j == 0 :
                    e2 = e2 * arr[i][j]
                else :
                    e1 = e1 * arr[i][j]
        return e1 - e2

def super_degree(arr) :
    li = []
    for i in range(len(arr)) :
        for j in range(1) :
            if i % 2 == 0 :
                li.append(arr[i][j])
            else :
                li.append(-arr[i][j])
    return li

def child_degree(arr) :
    li = []
    for i in range(len(arr)) :
        for j in range(1) :
            if i % 2 == 0 :
                li.append(arr[i][j])
            else :
                li.append(-arr[i][j])
    return li

def divide_arr(arr,r,c) :
    convertArr = []
    subArr = []
    for i in range(len(arr)) :
        for j in range(len(arr)) :
            if i == r or j == c :
                if c == len(arr) - 1 :
                    if len(subArr) != 0 :
                        convertArr.append(subArr)
                        subArr = []
                continue
            else :
                subArr.append(arr[i][j])
                
                if j == len(arr) - 1 :
                    convertArr.append(subArr)
                    subArr = []
                    
    return convertArr

A = [[ 2,0,3,-1],
    [ 1,0,2,2],
    [ 0,-1,1,4],
    [ 2,0,1,-3]]
    
for i in A :
    print(i)

super_d = super_degree(A)

total = 0
sum = 0
for j in range(len(super_d)) :
    X = divide_arr(A,j,0)
    ch_gree = child_degree(X)
    for l in range(len(ch_gree)) :
        P = divide_arr(X,l,0)
        sum = sum + ch_gree[l] * twobytwo_det(P)
    total = total + super_d[j] * sum
    sum = 0 
print('\n ∴ 주어진 행렬의 행렬식의 결과는',total)


