import numpy as np
import sympy as sp
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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


#######plotting##########
#range


def f(x):
    return eval(str(integral_symbolic))

x=np.linspace(a*0.8,b*(1.2))
y=f(x)

fig, ax=plt.subplots()
ax.plot(x,y, 'b', linewidth=2)
ax.set_ylim(bottom=0)

plt.title("Integral of f(x)")
ix=np.linspace(a, b)
iy=f(ix)
verts=[(a,0), *zip(ix, iy), (b, 0)]
poly= Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.text(0.4 * (a+b), f(b*1.1), r"$\int_" + str(int(a)) + "^" + str(int(b)) + "\hspace{1}" + sp.latex(integral_symbolic) + "\hspace{1}\mathrm{d}x$", horizontalalignment='center', fontsize=14)

fig.text(0.9, 0.05, "$x$")
fig.text(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a,b))
ax.set_xticklabels(('$' + str(int(a)) + "$", "$" + str(int(b)) + '$'))
ax.set_yticks([])

plt.show()

input("Press for exit..")