# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:47:26 2020
"""
import random, math, pylab, os

def dist(x,y):
    dx = abs(x[0] - y[0]) % 1.0
    dx = min(dx, 1.0 - dx)
    dy = abs(x[1] - y[1]) % 1.0
    dy = min(dy, 1.0 - dy)
    return  math.sqrt(dx**2 + dy**2)

def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()

filename = 'N60047710000.txt'


N = 64
N_sqrt = int(math.sqrt(N));
delxy = 1/(2*N_sqrt)
two_delxy = 2 * delxy
eta = 0.72
sigma_sq = eta/(N*math.pi)
sigma = math.sqrt(sigma_sq)
delta = 0.3 * sigma
n_steps = 10000
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print ('starting from file', filename)
else:
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
    print ('starting from a new random configuration')
for steps in range(n_steps):
    "We randomly choose a disk and move it a little."
    a = random.choice(L)
    "The disk is moved a little:"
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    b[0] = b[0]%1
    b[1] = b[1]%1
    min_dist = min(dist(b,c) for c in L if c != a)
    if not (min_dist < 2.0 * sigma ):
        a[:] = b
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L,sigma,'Final Config', 'initial.png')
print (L)