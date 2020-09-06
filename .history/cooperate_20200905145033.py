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
p=np.array([uuid.uuid1().int,sts.lognorm.rvs(.75)*100000,
sts.lognorm.rvs(.1)*50])
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
