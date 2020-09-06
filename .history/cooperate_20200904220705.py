#%%
import array as pArr
import numpy as np
import sympy as sym
import scipy as sc
import scipy.linalg as la
import matplotlib.pyplot as plt
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from Easy_Pretty_Math.Display_Math_Operations import *
# dmo_auto(status=True)
sym.init_printing(use_latex='mathjax', latex_mode='equation*')
# init_printing(pretty_print=True)
x, y, z, k, w = sym.symbols('x, y, z, k, w')
#%%
p=