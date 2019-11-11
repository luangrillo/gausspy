import numpy as np
import sympy as sp
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

#Calc valor of equation send by user
def funcao(eq, ti):
  x = ti
  return eval(eq)

def int_symbolic(integral_symbolic, a, b):
  x = a
  la = eval(integral_symbolic)
  x = b
  lb = eval(integral_symbolic)
  return lb-la

print('Calculation of numericall Integral by Gauss-Legendre Quadrature\n')

#Constants data
eq = input('Enter the equation to be validated (Python syntax): ')
a = float(input('Enter the lower limit:'))
b = float(input('Enter upper limit: '))
points = int(input('Enter the amount of points: '))

#Def points wi and ti
witi = np.polynomial.legendre.leggauss(points)

pontoseq=[]

#Calc of integral
integral_numerical = 0
for i in range(points):
  integral_numerical += witi[1][i] * funcao(eq, a+(b-a)/2*(witi[0][i]+1))
  pontoseq.append(integral_numerical)


print('\n\nIntegral by symbolic resolution:\n')
integral_symbolic = sp.integrate(eq)
print('Integral of', eq, ' and: ', integral_symbolic)
print('Numerical integral by gauss  = ', ((b-a)/2)*integral_numerical)
print('Exact integral = ', int_symbolic(str(integral_symbolic), a, b))

print('\n\nAbsolute error: ', abs(((b-a)/2)*integral_numerical-int_symbolic(str(integral_symbolic), a, b)))
print('Relative Error: ', abs((((b-a)/2)*integral_numerical-int_symbolic(str(integral_symbolic), a, b))/int_symbolic(str(integral_symbolic), a, b))*100, '%')

input("Press for exit..")

#######plotting##########
#range


x=np.arange(a, b, 0.1)
y=eval(str(integral_symbolic))

plt.plot(x, y)
plt.plot(pontoseq)
plt.legend(['Curva Original', 'Quadratura Leggauss'], loc='best')
plt.show()
