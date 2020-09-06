#%%
import numpy as np
import sympy as sym
import scipy as sc
import scipy.linalg as la
import matplotlib.pyplot as plt
import os
import nbformat
import tensorflow as tf
from nbconvert.preprocessors import ExecutePreprocessor
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# dmo_auto(status=True)
sym.init_printing(use_latex='mathjax', latex_mode='equation*')
# init_printing(pretty_print=True)
x, y, z, k, w = sym.symbols('x, y, z, k, w')
np.random.default_rng()
#%%
p=np.random.lognormal(100,100,1000)
# p=p.reshape(2500,1)
plt.hist(p, bins=200, density=True)
# %%
