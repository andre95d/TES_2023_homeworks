import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
"""
# Creazione di un vettore tempo
t = np.linspace(-1, 1, 1000)

# Creazione di una funzione rampa
ramp = np.maximum(0, t)

# Creazione di una funzione gradino unitario
step = np.heaviside(t, 1)

# Creazione di una funzione sinc
sinc = np.sinc(t)

# Creazione di una funzione triangolare
tri = np.maximum(0, 1 - np.abs(t))

# stem delle funzioni
plt.stem(t, ramp, label='Rampa')
plt.stem(t, step, label='Gradino')
plt.stem(t, sinc, label='Sinc')
plt.stem(t, tri, label='Triangolare')
plt.legend()
plt.ion()
"""
#inizio lab1_ex1
#ex1

def x_n(n):
    if n < 0 or n > 10:
        return 0
    else:
        return n

# time vector initialization
t = np.arange(-5, 16) 

#dirac impulse distribution definition, given the 1st parameter of np.arange() 
def dirac(n=0):
    return signal.unit_impulse(len(t), idx=n+5)

# y[n] vector initialization for each ex.
y_a = [x_n(n+5) for n in t]
y_b = [x_n(-n+5) for n in t]
y_c = [x_n(2*n) for n in t]
 
def x_nd(n):
    return x_n(n+10) + x_n(-n+10) 
y_d = [x_nd(n) for n in t] - (10*dirac(0))

# stem della funzione y[n]
plt.subplot(4,1,1)
plt.stem(t, y_a, linefmt='r-', label='y_a[n]')
plt.subplot(4,1,2)
plt.stem(t, y_b, linefmt='b-',label='y_b[n]')
plt.subplot(4,1,3)
plt.stem(t, y_c, linefmt='g-',label='y_c[n]')
plt.subplot(4,1,4)
plt.stem(t, y_d, linefmt='y-', label='y_d[n]')
plt.title('ex1.abcd')
plt.xlabel('t')
plt.ylabel('y[n]')
plt.legend()
plt.grid()
plt.show()
