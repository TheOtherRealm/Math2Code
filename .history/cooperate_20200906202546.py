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
import copy
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
numOfP=50
#Array of people's ids
ids=sp.array(range(0,numOfP),dtype='int64')
#People object
p=[];
#Populate people with attributes
for id in ids:
	p.append((
		id,
		#people's value
		sts.lognorm.rvs(.3)*100000,
		#people's ability
		(1/(sts.lognorm.rvs(.99)+1))
		#entropy required to get help
	))
p=np.array(p,dtype=[('id','int64'),('value','float64'),('ability','float32')])

# plt.plot(p[1])
plt.hist(p['value'],bins=200,  density=True)
# %%
history=[copy.deepcopy(p)]
def runSim(t):
	cnt=0
	i=0
	while i<t:
		# print('itter:',i)
		for id,value,ability in p:
			entropy=(1/(sts.lognorm.rvs(.99)+1))*.1
			if(p['value'][(cnt+1)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt+1)%numOfP]+=(value*abs(ability-entropy))
				p['value'][cnt]-=(value*abs(ability-entropy))
			elif(p['value'][(cnt-1)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt-1)%numOfP]+=(value*abs(ability-entropy))
				p['value'][cnt]-=(value*abs(ability-entropy))
			elif(p['value'][(cnt-2)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt-1)%numOfP]+=abs(value*(ability-entropy))
				p['value'][cnt]-=(value*abs(ability-entropy))
			elif(p['value'][(cnt+2)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt-1)%numOfP]+=(value*abs(ability-entropy))
				p['value'][cnt]-=(value*abs(ability-entropy))
			# print(p['value'][cnt],(value*(ability-entropy)))
			# print(p['value'][cnt],(value*(ability-entropy)))
			cnt+=1
		i+=1;
		history.append([i,copy.deepcopy(p)])
		cnt=0
runSim(1000)
historyA=np.asarray(history)
#%%
# print(history[1])
print(history[999:1000])
# %%
p['value']
# %%
