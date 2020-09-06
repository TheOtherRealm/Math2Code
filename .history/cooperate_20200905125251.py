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
#%%
p=np.random.default_rng().normal(50,25,100)
# p=p.reshape(2500,1)
plt.plot(p)
# %%
