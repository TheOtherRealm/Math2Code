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
numOfP=10
#Array of people's ids
ids=[uuid.uuid1().int for n in range(0,numOfP)]
ids=sp.array(ids,dtype='U128')
#People object
# p=np.array(p,dtype=[('id','int'),('value','float'),('ability','float')]);
p=[];
#Populate people with attributes
for id in ids:
	p.append((
		id,
		#people's value
		sts.lognorm.rvs(.7)*100000,
		#people's ability
		(1/(sts.lognorm.rvs(.99)+1))
	))
p=np.array(p,dtype=[('id','U128'),('value','float64'),('ability','float32')]);
# plt.plot(p[1])
# %%
plt.hist(p[:,0], bins=200, density=True)
# %%
def runSim(t):
	while t>0:
		for id in p[:,0]:
			print(id)
		t=t-1
runSim(10)
# %%
