# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:54:09 2020
"""

import random, pylab

def markov_disks_box():
    histo_data = []
    L = [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)]
    sigma = 0.1197
    sigma_sq = sigma ** 2
    delta = 0.1
    n_steps = 2000000
    a = random.choice(L)
    for steps in range(n_steps):
        randomNumber = random.choice([0,1,2,3])
        a = L[randomNumber]
        "The disk is moved a little:"
        b = (a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta))
        "We check that the new movement is valid"
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            L[randomNumber] = b    
        for k in range(4):
            histo_data.append(L[k][0])
    pylab.hist(histo_data, bins=100)
    pylab.xlabel('x')
    pylab.ylabel('frequency')
    pylab.title('Markov sampling: x coordinate histogram (density eta=0.18)')
    pylab.grid()
    pylab.savefig('Markov_disks_histo.png')
    pylab.show()
    return L

markov_disks_box()