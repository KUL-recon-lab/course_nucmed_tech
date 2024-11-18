# unit impulse response of the two tissue comparment model

from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols, pprint
from sympy.solvers.ode.systems import dsolve_system
from sympy.abc import x

f1 = Function('f1')
f2 = Function('f2')
K1 = symbols('K1', positive=True)
k2 = symbols('k2', positive=True)
k3 = symbols('k3', positive=True)
k4 = symbols('k4', positive=True)

# set k4 to 0 for the FDG model
#k4 = 0

ode1 = Eq(Derivative(f1(x), x), -(k2+k3) * f1(x) + k4*f2(x))
ode2 = Eq(Derivative(f2(x), x), k3 * f1(x) - k4 * f2(x))

# unit impulse response is repose to C_a(t) = delta(t)
# technically the same as solving the homogeous part with the boundary
# condition f1(0) = K1 and f2(0) = 0

sol = dsolve_system([ode1,ode2], ics = {f1(0): K1, f2(0): 0})

pprint(sol[0][0])
pprint(sol[0][1])
