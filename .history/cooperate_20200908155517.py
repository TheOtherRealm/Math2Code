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
numOfP=5
#Array of people's ids
ids=np.array(range(0,numOfP),dtype='int64')
z=np.zeros(numOfP)
#People object
temp=[];
peoType=dtype=[
	('id','int64'),
	('value','float64'),
	('ability','float32'),
	('helpNeeded','float32'),
	('helpOut','object'),
	('helpIn','object')
]
#Populate people with attributes
for id in ids:
	temp.append([
		#0 - id
		id,
		#1 - people's value
		sts.lognorm.rvs(.5)*100000,
		#2 - people's ability
		(1/(sts.lognorm.rvs(.99)+1)),
		#3 - help needed
		((sts.lognorm.rvs(.99))*100),
		#4 - people helped
		copy.deepcopy(z),
		#5 - people who helped you
		copy.deepcopy(z)
	])
# tempA=np.array(temp,dtype='object')
temp
peo=np.array(temp,peoType)
# np.sum(peo['value'])
# plt.plot(p[1])
# %%
history=[copy.deepcopy(peo)]
def runSim(t,p):
	cnt=0
	i=0
	while i<t:
		# print('itter:',i)
		for id,value,ability,helpNeeded,helpOut in p:
			lowest=np.where(p['value'] == np.amin(p['value']))
			amountToTransfer=((value-p['value'][lowest[0][0]])*(ability))
			amountToTransfer-=((sts.lognorm.rvs(.99))*100)
			# print(cnt,amountToTransfer)
			p['value'][lowest[0]]+=amountToTransfer
			p['value'][cnt]-=amountToTransfer
			cnt+=1
		i+=1;
		history.append([i,copy.deepcopy(p)])
		cnt=0

runSim(1000,peo)
historyA=np.asarray(history)
#%%
print(history[0:1])
print(history[999:1000])
# %%
peo['value']
# %%
'''
			entropy=(1/(sts.lognorm.rvs(.99)+1))*.1
			if(p['value'][(cnt+1)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt+1)%numOfP]+=(value*abs(ability))
				p['value'][cnt]-=(value*abs(ability))
			elif(p['value'][(cnt-1)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt-1)%numOfP]+=(value*abs(ability))
				p['value'][cnt]-=(value*abs(ability))
			elif(p['value'][(cnt-2)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt-1)%numOfP]+=abs(value*(ability))
				p['value'][cnt]-=(value*abs(ability))
			elif(p['value'][(cnt+2)%numOfP]<p['value'][(cnt)%numOfP]):
				p['value'][(cnt-1)%numOfP]+=(value*abs(ability))
				p['value'][cnt]-=(value*abs(ability))
			# print(p['value'][cnt],(value*(ability)))
			# print(p['value'][cnt],(value*(ability)))
'''
#%%
plt.hist(p['value']*((sts.lognorm.rvs(.99)+1)*100),bins=200,  density=True)
# %%
