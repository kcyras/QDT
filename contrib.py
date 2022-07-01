#!/usr/bin/env python3

import sympy as sp
sp.init_printing()

a, b, c, d, e, f = sp.symbols('a b c d e f')  # arguments
E_a, E_b, E_c, E_d, E_e, E_f = sp.symbols('E_a E_b E_c E_d E_e E_f')
    # E_x - symbolic variable for the energy of argument x

energy, initial = sp.symbols('energy initial')
impact = lambda energy : sp.Max(0, energy)**2 / (1 + sp.Max(0, energy)**2)
combine = lambda initial, energy : initial - initial*impact(-energy) + (1-initial)*impact(energy)

print("STRENGTHS.")

E_f = 0  # f has no children
fs_f = combine(f, E_f)
    # fs_x - symbolic variable for the final strength of argument x
f_initial = f.evalf(subs={f: 1.0}, chop=True)
    # x_initial - initial strength of argument x
f_final = fs_f.evalf(subs={f: f_initial})
    # x_final - final strength of argument x
print(f"{f}: ({f_initial}) {f_final};")

E_e = 0  # e has no children
fs_e = combine(e, E_e)
e_initial = e.evalf(subs={e: 0.4}, chop=True)
e_final = fs_e.evalf(subs={e: e_initial})
print(f"{e}: ({e_initial}) {e_final};")

E_d = 0  # d has no children
fs_d = combine(d, E_d)
d_initial = d.evalf(subs={d: 0.65}, chop=True)
d_final = fs_d.evalf(subs={d: d_initial})
print(f"{d}: ({d_initial}) {d_final};")

E_c = fs_e - fs_f  # c is supported by e and attacked by f
fs_c = combine(c, E_c)
c_initial = c.evalf(subs={c: 0.85}, chop=True)
c_final = fs_c.evalf(subs={c: c_initial, e: e_initial, f: f_initial})
print(f"{c}: ({c_initial}) {c_final};")

E_b = -fs_e  # e is the only attacker of b
fs_b = combine(b, E_b)
b_initial = b.evalf(subs={b: 0.2}, chop=True)
b_final = fs_b.evalf(subs={b: b_initial, e: e_initial})
print(f"{b}: ({b_initial}) {b_final};")

E_a = fs_b + fs_d - fs_c
fs_a = combine(a, E_a)
a_initial = a.evalf(subs={a: 0.5}, chop=True)
a_final = fs_a.evalf(subs={a: a_initial, b: b_initial, c: c_initial, d: d_initial, e: e_initial, f: f_initial})
print(f"{a}: ({a_initial}) {a_final};")

pdfs_a_a = fs_a.diff(a)
pdfs_a_b = fs_a.diff(b)
pdfs_a_c = fs_a.diff(c)
pdfs_a_d = fs_a.diff(d)
pdfs_a_e = fs_a.diff(e)
pdfs_a_f = fs_a.diff(f)

print("Ctrb to a from a: ", pdfs_a_a.evalf(subs={a: a_initial, b: b_initial,
    c: c_initial, d: d_initial, e: e_initial, f: f_initial}, chop=True))
print("Ctrb to a from b: ", pdfs_a_b.evalf(subs={a: a_initial, b: b_initial,
        c: c_initial, d: d_initial, e: e_initial, f: f_initial}, chop=True))
print("Ctrb to a from c: ", pdfs_a_c.evalf(subs={a: a_initial, b: b_initial,
        c: c_initial, d: d_initial, e: e_initial, f: f_initial}, chop=True))
print("Ctrb to a from d: ", pdfs_a_d.evalf(subs={a: a_initial, b: b_initial,
        c: c_initial, d: d_initial, e: e_initial, f: f_initial}, chop=True))
print("Ctrb to a from e: ", pdfs_a_e.evalf(subs={a: a_initial, b: b_initial,
        c: c_initial, d: d_initial, e: e_initial, f: f_initial}, chop=True))
print("Ctrb to a from f: ", pdfs_a_f.evalf(subs={a: a_initial, b: b_initial,
        c: c_initial, d: d_initial, e: e_initial, f: f_initial}, chop=True))
