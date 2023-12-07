import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
BEGIN = 0
t = np.arange(BEGIN, 15)
#FIXME: convolve() gives strange values if BEGIN<0
def delta(n=0):
    return signal.unit_impulse(len(t), idx= -BEGIN + n)

x_1 = delta(0) + 2*delta(1) + delta(2)
x_2 = 3*delta(0) + 2*delta(1) + delta(2)

plt.subplot(3,1,1)
plt.stem(t, x_1, linefmt='r-', label='x_1[n]')
plt.subplot(3,1,2)
plt.stem(t, x_2, linefmt='b-',label='x_2[n]')
result = np.convolve(x_1, x_2, mode='full')
plt.subplot(3,1,3)
plt.stem(result, linefmt='b-',label='convolve(x_1,x_2)')
plt.title('ex2')
plt.xlabel('n')
plt.ylabel('convolve() result')
plt.legend()
plt.grid()
plt.show()
print(x_1, x_2)