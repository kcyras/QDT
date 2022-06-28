#!/usr/bin/env python3

import numpy as np
# from jax import grad

import sympy as sp
sp.init_printing()

a, b, c, d, e = sp.symbols('a b c d e')  # arguments

E_a, E_b, E_c, E_d, E_e = sp.symbols('E_a E_b E_c E_d E_e')
    # E_x - symbolic variable for the energy of argument x

energy, initial = sp.symbols('energy initial')
impact = lambda energy : sp.Max(0, energy)**2 / (1 + sp.Max(0, energy)**2)
combine = lambda initial, energy : initial - initial*impact(-energy) + (1-initial)*impact(energy)

print("STRENGTHS.")

E_e = 0  # e has no children
fs_e = combine(e, E_e)
    # fs_x - symbolic variable for the final strength of argument x
e_initial = e.evalf(subs={e: 1.0}, chop=True)
    # x_initial - initial strength of argument x
e_final = fs_e.evalf(subs={e: e_initial})
    # x_final - final strength of argument x
print(f"{fs_e}: ({e_initial}) {e_final};")

E_d = 0  # d has no children
fs_d = combine(d, E_d)
d_initial = d.evalf(subs={d: 0.5}, chop=True)
d_final = fs_d.evalf(subs={d: d_initial, e: e_initial})
print(f"{fs_d}: ({d_initial}) {d_final};")

E_c = fs_e  # e is the only supporter of c
fs_c = combine(c, E_c)
c_initial = c.evalf(subs={c: 0.5}, chop=True)
c_final = fs_c.evalf(subs={c: c_initial, e: e_initial})
print(f"{fs_c}: ({c_initial}) {c_final};")

E_b = -fs_e  # e is the only attacker of b
fs_b = combine(b, E_b)
b_initial = b.evalf(subs={b: 0.5}, chop=True)
b_final = fs_b.evalf(subs={b: b_initial, e: e_initial})
print(f"{fs_b}: ({b_initial}) {b_final};")

E_a = fs_b + fs_d - fs_c
fs_a = combine(a, E_a)
a_initial = a.evalf(subs={a: 0.5}, chop=True)
a_final = fs_a.evalf(subs={a: a_initial, b: b_initial, c: c_initial, d: d_initial, e: e_initial})
print(f"{fs_a}: ({a_initial}) {a_final};")

pdfs_a_b = fs_a.diff(b)
pdfs_a_c = fs_a.diff(c)
pdfs_a_d = fs_a.diff(d)
pdfs_a_e = fs_a.diff(e)

pdfs_a_b_eval = sp.lambdify([a, b, c, d, e], pdfs_a_b, 'numpy')
print("Ctrb to a from b: ", pdfs_a_b_eval(a_initial, b_initial, c_initial, d_initial, e_initial))
pdfs_a_c_eval = sp.lambdify([a, b, c, d, e], pdfs_a_c, 'numpy')
print("Ctrb to a from c: ", pdfs_a_c_eval(a_initial, b_initial, c_initial, d_initial, e_initial))
pdfs_a_d_eval = sp.lambdify([a, b, c, d, e], pdfs_a_d, 'numpy')
print("Ctrb to a from d: ", pdfs_a_d_eval(a_initial, b_initial, c_initial, d_initial, e_initial))
pdfs_a_e_eval = sp.lambdify([a, b, c, d, e], pdfs_a_e, 'numpy')
print("Ctrb to a from e: ", pdfs_a_e_eval(a_initial, b_initial, c_initial, d_initial, e_initial))
