#%%
import numpy as np
import sympy as sym
import scipy as sp
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
numOfP=10
ids=[uuid.uuid1().int for n in range(0,numOfP)]
ids=sp.array(ids)
moneys=[sts.lognorm.rvs(.75)*100000 for n in range(0,numOfP)]
moneys=sp.array(money)
abilities=[(1/(sts.lognorm.rvs(.5)+1)) for n in range(0,numOfP)]
abilities=sp.array(ability)
# ids,money,ability
p={}
for id in ids:
	p[id]=[sts.lognorm.rvs(.75)*100000,(1/(sts.lognorm.rvs(.5)+1))]
p
# %%
plt.hist(sts.lognorm.rvs(.1,size=1000)*50, bins=200, density=True)
# %%
id=uuid.uuid1()
id
# %%
id.int
# %%
