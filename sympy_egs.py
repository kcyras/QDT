#!/usr/bin/env python3

import numpy as np
import sympy as sp
sp.init_printing()

x, y = sp.symbols('x, y')
first = lambda x : x**2
second = lambda x, y : first(x)*y
third = second(x, y).subs([(x, 2.0), (y, first(x))])
print(second(x, y).args)
print(f"second function {second(x, y)} differentiated wrt y: {sp.diff(second(x, y), y)}")
print(f"third function {third}")
print(f"Equality: {sp.Eq(second(x, y), 4)}")
print(f"Unevaluated derivative {sp.Derivative(second(x, y), x)}"
    f" evaluated: {sp.Derivative(second(x, y), x).doit()}")

z = sp.Symbol('z')
function = sp.sympify("z**2 + 2*z + 1")
derivative = function.diff()
print(f"sympyfied function {function} (with derivative {derivative}) "
    f"evaluated at z=0 to equal {function.evalf(subs={z: 0}, chop=True)}")
der = sp.lambdify(z, derivative, 'numpy')
print(f"lambdified {derivative} as {der} and numpy-evaluated at z=0 to equal {der(0)}")
