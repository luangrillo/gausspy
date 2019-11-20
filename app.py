import numpy as np
import sympy as sp
from numpy import *
from appJar import gui
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Calc valor of equation send by user
def funcao(eq, ti):
    x = ti
    return eval(eq)


def int_symbolic(integral_symbolic, a, b):
    x = a
    la = eval(integral_symbolic)
    x = b
    lb = eval(integral_symbolic)
    return lb-la


# GUI

def press(click):

    app.setSize("550x800")
    eq = app.getEntry("Equation on python syintax")
    a = float(app.getEntry("Lower limit"))
    b = float(app.getEntry("Upper limit"))
    points = int(app.getEntry('Enter the amount of points: '))

    # Def points wi and ti
    witi = np.polynomial.legendre.leggauss(points)

    pontoseq = []

    # Calc of integral
    integral_numerical = 0
    for i in range(points):
        integral_numerical += witi[1][i] * funcao(eq, a+(b-a)/2*(witi[0][i]+1))
        pontoseq.append(integral_numerical)

        integral_symbolic = sp.integrate(eq)

    longstring = str('Integral by symbolic resolution:\n'
                     + 'f(x) = ' + eq 
                     + '\nIntegral symbolic: ' + str(integral_symbolic)
                     + '\nNumerical integral by gauss  = '
                     + str(((b-a)/2)*integral_numerical)
                     + '\nExact integral = '
                     + str(int_symbolic(str(integral_symbolic), a, b))
                     + '\n\nAbsolute error: ' +
                     str(abs(((b-a)/2) * integral_numerical -
                             int_symbolic(str(integral_symbolic), a, b)))
                     + '\nRelative Error: ' + str(abs((((b-a)/2)*integral_numerical-int_symbolic(str(integral_symbolic), a, b))/int_symbolic(str(integral_symbolic), a, b))*100) +
                     "%")

   

    #######plotting##########
    # range

    def f(x):
        return eval(str(integral_symbolic))

    x = np.linspace(a*0.8, b*(1.2))
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'b', linewidth=2)
    ax.set_ylim(bottom=0)

    plt.title("Integral of f(x)")
    ix = np.linspace(a, b)
    iy = f(ix)
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    ax.text(0.4 * (a+b), f(b*1.1), r"$\int_" + str(int(a)) + "^" + str(int(b)) + "\hspace{1}" + sp.latex(
        integral_symbolic) + "\hspace{1}\mathrm{d}x$", horizontalalignment='center', fontsize=14)

    fig.text(0.9, 0.05, "$x$")
    fig.text(0.1, 0.9, '$y$')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.xaxis.set_ticks_position('bottom')

    ax.set_xticks((a, b))
    ax.set_xticklabels(('$' + str(int(a)) + "$", "$" + str(int(b)) + '$'))
    ax.set_yticks([])

    plt.savefig('figure.png')

    app.addLabelEntry(longstring)
    app.addImage("Grapich", "figure.png")



# End of def

app = gui("GaussPy", "550x200")


app.addLabel(
    "title", "Calculator Integral by Gauss-Legendre Quadrature")

app.addLabelEntry("Equation on python syintax")
app.addLabelEntry("Upper limit")
app.addLabelEntry("Lower limit")
app.addLabelEntry('Enter the amount of points: ')

app.addButtons(["Run"], press)


app.go()

