#%%
import numpy as np
import sympy as sym
import scipy as sc
import scipy.linalg as la
import scipy.stats as sts
import matplotlib.pyplot as plt
import os
import uuid
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
p=np.array([
	#id
	uuid.uuid1().int,
	#money
	sts.lognorm.rvs(.75)*100000,
	#
	(1/(sts.lognorm.rvs(.5)+1))
] in n for range(0,10))
# p=p.reshape(2500,1)
# 
p
# %%
plt.hist(sts.lognorm.rvs(.1,size=1000)*50, bins=200, density=True)
# %%
id=uuid.uuid1().int
id
# %%
id.int
# %%
