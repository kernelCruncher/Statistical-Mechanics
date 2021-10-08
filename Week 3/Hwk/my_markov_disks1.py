# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:47:26 2020
"""
import random, math

def dist(x,y):
    dx = abs(x[0] - y[0]) % 1.0
    dx = min(dx, 1.0 - dx)
    dy = abs(x[1] - y[1]) % 1.0
    dy = min(dy, 1.0 - dy)
    return  math.sqrt(dx**2 + dy**2)


L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 1000
for steps in range(n_steps):
    "We randomly choose a disk and move it a little."
    a = random.choice(L)
    "The disk is moved a little:"
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    b[0] = b[0]%1
    b[1] = b[1]%1
    min_dist = min(dist(b,c) for c in L if c != a)
    if not (min_dist < 2.0 * sigma):
        a[:] = b
print (L)