import numpy as np  
import matplotlib.pyplot as plt  

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)  
    plt.show()  

def my_formula(x):
    return x**3+2*x-4

graph(my_formula, range(-10, 11))


####do derivatives

import sympy

x = sympy.Symbol('x')
y = (sympy.exp(-.0482 * x) * 100)
yprime = y.diff(x) # get derivative
print yprime # print derivative
print y.diff(x, 5)