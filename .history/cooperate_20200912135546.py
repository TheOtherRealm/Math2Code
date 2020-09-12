#%%
import numpy as np
from numpy.lib import recfunctions as rfn
import sympy as sym
import scipy as sp
import scipy.linalg as la
import scipy.stats as sts
import pandas as pd
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
def as_dict(rec):
    """ turn a numpy recarray record into a dict. this is mostly useful
    just to have a human readable output of a record on the console.
    
    as_dict(my_data[234])
    """
    
    return {name:rec[name] for name in rec.dtype.names}
#%%
#Number of People
numOfP=5
#Array of people's ids
ids=np.array(range(0,numOfP),dtype='int64')
z=np.zeros(numOfP)
#People object
peo={};
peoType=np.dtype({
	'names':
	['id','value','ability','helpNeeded','helpOut','helpIn'],
	'formats':
	['int64', 'float64', 'float32', 'float32', 'object', 'object']
});
#Populate people with attributes
'''
	temp.append((
		#0 - id
		np.array([id]),
		#1 - people's value
		np.array([sts.lognorm.rvs(.5)*100000]),
		#2 - people's ability
		np.array([(1/(sts.lognorm.rvs(.99)+1))]),
		#3 - help needed
		np.array([((sts.lognorm.rvs(.99))*100)]),
		#4 - people helped
		np.zeros(numOfP),
		#5 - people who helped you
		np.zeros(numOfP)
	))
'''
for id in range(numOfP):
	peo[id]=[
		#1 - people's value
		{'value':np.array([sts.lognorm.rvs(.5)*100000])},
		#2 - people's ability
		{'ability':np.array([(1/(sts.lognorm.rvs(.99)+1))])},
		#3 - help needed
		{'helpNeeded':np.array([((sts.lognorm.rvs(.99))*100)])},
		#4 - people helped
		{'helpOut':np.zeros(numOfP)},
		#5 - people who helped you
		{'helpIn':np.zeros(numOfP)}
	]
# temp=np.asarray(temp)
# rfn.unstructured_to_structured(temp,peoType)
# temp
# %%
# peo=np.array(temp,dtype=peoType)

history[0]=copy.deepcopy(peo)
def runSim(t,p):
	cnt=0
	i=0
	while i<t:
		# print('itter:',i)
		for id,value,ability,helpNeeded,helpOut,helpIn in p:
			lowest=np.where(p['value'] == np.amin(p['value']))
			amountToTransfer=((value-p['value'][lowest[0][0]])*(ability))
			amountToTransfer-=((sts.lognorm.rvs(.99))*100)
			# print(cnt,amountToTransfer)
			p['value'][lowest[0]]+=amountToTransfer
			p['value'][cnt]-=amountToTransfer
			cnt+=1
		i+=1;
		history[i]=copy.deepcopy(peo)
		cnt=0
runSim(2,peo)
#%%
print(history[0][0][1])
# print('~~~~~~~~~~~~~~~~~~~~~~~~')
# print(history[999:1000])
# %%
history['value']
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
plt.hist(peo['value']*((sts.lognorm.rvs(.99)+1)*100),bins=200,  density=True)
# %%
plt.plot(history[990:1000][1][0][1])

# %%
historyA[999:1000]
# %%
s=pd.Series(history)
s #['value']
# plt.plot(x,s[x]['value'])
# %%
