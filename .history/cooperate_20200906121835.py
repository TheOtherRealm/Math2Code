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
x, y, z, k, w; # sym.symbols('x, y, z, k, w')
np.random.default_rng()
#%%
#Number of People
numOfP=1000
#Array of people's ids
ids=[uuid.uuid1().int for n in range(0,numOfP)]
ids=sp.array(ids)
#People object
p=[];
#Populate people with attributes
for id in ids:
	p.append([
		id,
		#people's value
		sts.lognorm.rvs(.7)*100000,
		#people's ability
		(1/(sts.lognorm.rvs(.99)+1))
	])
p=np.array(p,dtype='float32')
# plt.plot(p[1])
# %%
plt.hist(p[:,2], bins=200, density=True)
# %%
def 