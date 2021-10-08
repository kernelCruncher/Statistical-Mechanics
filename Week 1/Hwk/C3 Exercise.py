# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:09:27 2020
"""

import random, math
n_trials = 400000
n_hits = 0
var = 0.0
sumObs=0
sumObs2=0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    sumObs+=Obs
    sumObs2+=Obs*Obs
    
print( sumObs/n_trials, sumObs2/n_trials, sumObs2/n_trials - (sumObs/n_trials)**2 , math.sqrt(sumObs2/n_trials - (sumObs/n_trials)**2 ))