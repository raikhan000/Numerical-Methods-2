import numpy as np
import matplotlib.pyplot as plt
import time 
eps = 0.2
def Jacobi(A, f):
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
		if a < eps:
			flag = 1
		else:
			x = x_new.copy()
	return x


time_1 = np.zeros(10)
time_2 = np.zeros(10)
for m in range(10):
	m = m + 1
	n = m*100		
	A = np.random.rand(n,n)
	f = np.random.rand(n)
	
	s = np.sum(np.abs(A), axis = 1)
	for i in range(n):
		A[i][i] = A[i][i] + s[i]

	timer_start = time.time()
	x = Jacobi(A, f)
	time_1[m - 1] = time.time() - timer_start

	timer_start = time.time()
	x_compare = np.linalg.solve(A, f)
	time_2[m - 1] = time.time() - timer_start
	
	print('Для n =',n,'||x - x_compare|| = ', np.linalg.norm(x_compare - x))

for i in range(10):
	print(i+1,':','Время для метода Якоби = ',time_1[i], '|','Время scipy.linalg.solve =', time_2[i])

plt.plot(time_1)
plt.plot(time_2)
plt.show()


