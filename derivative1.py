import sympy as smp
from scipy.misc import derivative

x, a, b, c = smp.symbols('x a b c', real=True)
f = smp(x**2)
# f = smp.exp(-a*smp.sin(x**2))


dfdx = smp.diff(f,x)
print(dfdx)