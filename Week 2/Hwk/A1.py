# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:06:02 2020
"""

import random, math
"Sigma is the radius, here."
def direct_disks_box(N, sigma):
    condition = False
    while condition == False:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        "N is the number of harddisks in the configuration"
        "This directly sampling 4 disks. If they are too close then the process is reset - Tabula Rasa."
        for k in range(1, N):
            a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
            min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L)
            "If the hard disks are too close together then this is a violation.s"
            if min_dist < 2.0 * sigma:
                condition = False
                break
            else:
                L.append(a)
                condition = True
    return L


sigma = 0.15
del_xy = 0.05
n_runs = 10**6
conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}

for run in range(n_runs):
    "We compute the n_runs of different configurations"
    x_vec = direct_disks_box(4, sigma)
    for conf in configurations:
        condition_hit = True
        "This is checking if the configurations, i.e. conf(a), conf(b), conf(c), are sufficientky close to the x_vec"
        for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
            condition_hit *= condition_b
        if condition_hit:
            hits[conf] += 1

for conf in configurations:
    print (conf, hits[conf])#