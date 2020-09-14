# %%
import numpy as np
import sympy as sy
import scipy as sc
sy.init_printing(use_latex='mathjax', latex_mode='equation*')
x, y, z, k, w = sy.symbols('x, y, z, k, w')

# %%
'''
The rank of a matrix A, written rank(A), is the dimension of the column space Col(A) 
'''

# %%
A = sy.Matrix([
	[0, 6, 8], 
	[.5, 0, 0], 
	[0, .5, 0]])
A
A.rank()

# %%
((22*.1)+22)*11
# %%
