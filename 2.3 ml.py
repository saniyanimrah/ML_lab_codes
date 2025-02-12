# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:24:02 2025

@author: pc
"""

import scipy.optimize as opt
def objective(x):
    return x[0]**2 + x[1]**2
result = opt.minimize(objective,[1,1])
print(f"opt sol:{result.x}")
from scipy.integrate import quad
def integrand(x):
    return x**2
area,error = quad(integrand,0,2)
print(f"integral result:{area:.2f}")