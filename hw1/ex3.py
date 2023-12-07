import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from sympy import limit, symbols
t = np.arange(-5, 16)
#ex3.a
def x1_n(n):
     if n>=0:
        return np.exp(-n)
     else: return 0

E_x1 = np.sum(np.square([x1_n(n) for n in t]))
print(E_x1)
#E_x1 < inf: energia finita <-> potenza nulla
""""""
#ex3.b
A = symbols("A")
N = symbols("N")
#sappiamo già che è a energia -> inf avendo supporto illimitato
#calcoliamo la potenza media
x2_f = ((1/(2*N+1))) * (2*N +1) * np.square(A)
E_x2 = limit(x2_f, N, float('inf'))

print(E_x2) #Output: A**2
""""""
#ex3.c
complex()

"""
plt.subplot(1,1,1)
plt.stem(t, x1_n(t), linefmt='r-', label='y_a[n]')
plt.subplot(4,1,2)
plt.stem(t, y_b, linefmt='b-',label='y_b[n]')
plt.subplot(4,1,3)
plt.stem(t, y_c, linefmt='g-',label='y_c[n]')
plt.subplot(4,1,4)
plt.stem(t, y_d, linefmt='y-', label='y_d[n]')
plt.title('ex3')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend()
plt.grid()
plt.show()
"""