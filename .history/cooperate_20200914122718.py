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
#Number of People
numOfP=5
#Array of people's ids
z=np.zeros(numOfP)
#People object
peo={};
for id in range(numOfP):
	peo[id]={
		#1 - people's value
		'value':np.array([sts.lognorm.rvs(.5)*75000]),
		#2 - people's ability
		'ability':np.array([(1/(sts.lognorm.rvs(.99)*100))]),
		#3 - help needed
		'helpNeeded':np.array([(1/(sts.lognorm.rvs(.99)+1))*100]),
		#4 - people helped
		'helpOut':np.zeros(numOfP),
		#5 - people who helped you
		'helpIn':np.zeros(numOfP)
	}
totalValue=0
[v['value'] for v in peo.values()]
for sum in [v['value'] for v in peo.values()]:
	totalValue+=sum
totalValue
peo
# %%
history[0]=peo
def runSim(t,p):
	cnt=0
	i=0
	j=0
	while j<t:
		while i<len(p):
			poorest=min(p, key=lambda v: p[v]['value'])
			lowestW=p[poorest]['value']
			# needMostHelp=max(p, key=lambda v: p[v]['helpNeeded'])
			# print(poorest,lowest)
			amountToTransfer=((p[i]['value']-lowestW)-(p[poorest]['helpNeeded']))
			amountToTransfer-=((sts.lognorm.rvs(.99))*100)
			p[poorest]['value']+=amountToTransfer
			p[i]['value']-=amountToTransfer-(p[i]['ability'])
			p[poorest]['helpIn'][i]+=1
			p[i]['helpOut'][poorest]+=1
			cnt+=1
			i+=1;
		j+=1
		i=0
		history[j]=peo
		cnt=0
runSim(100,peo)
#%%
[v['value'] for v in peo.values()]
peo
# print(history)
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
