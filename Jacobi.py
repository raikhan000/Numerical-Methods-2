from math import*
import numpy as np

def Jacobi(A, f, eps):
	n = int(len(f))
	x = np.zeros(n)
	x_new = np.zeros(n)
	flag = 0
	while flag != 1:
		for i in range(n):
			s = 0
			s1  = 0
			for j in range(i-1):
				s = s + A[i][j]*float(x[j])
			for j in range(i+1, n):
				s = s + A[i][j]*float(x[j])
			x_new[i] = (f[i]- s) / A[i][i]
		a = np.linalg.norm(x_new - x)
		if a**2 < eps**2:
			flag = 1
		else:
			x = x_new.copy()
	return x

print('Введите размер матрицы nxn:')
n = int(input())
f = np.zeros(n)
print('Введите матрицу A')
A = [[float(j) for j in input().split()] for i in range(n)]
print('Введите вектор свободных членов размера n')
f = [float(i) for i in input().split()]
print("Введите точность")
eps = float(input())
print(Jacobi(A, f, eps))

print("Проверка решения:")
print(np.linalg.solve(A, f))


