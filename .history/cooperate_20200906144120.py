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
x, y, z, k, w=sym.symbols('x, y, z, k, w')
np.random.default_rng()
np.set_printoptions(suppress=True)
#%%
#Number of People
numOfP=5
#Array of people's ids
ids=[uuid.uuid1().int for n in range(0,numOfP)]
ids=sp.array(ids,dtype='U128')
#People object
p=[];
#Populate people with attributes
for id in ids:
	p.append((
		id,
		#people's value
		sts.lognorm.rvs(.7)*10,
		#people's ability
		(1/(sts.lognorm.rvs(.99)+1))
	))
p=np.array(p,dtype=[('id','U128'),('value','float64'),('ability','float32')]);
# plt.plot(p[1])
# %%
plt.hist(p['ability'], bins=200, density=True)
# %%
def runSim(t):
	cnt=0
	while t>0:
		print('itter:',t)
		for id,value,ability in p:		
			p['value'][cnt]+=(value*ability)
			print(p['value'][cnt])
			cnt+=1
		t-=1;
		cnt=0
runSim(10)
# %%
p['value']
# %%
