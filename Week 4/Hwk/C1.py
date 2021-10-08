import random, pylab

d_max = 200
dict = {}

for d in range(1, d_max):
    x = [0] * d
    delta = 0.05
    n_trials = 4000
    n_hits = 0
    rList = []
    for i in range(n_trials):
        k = random.randint(0, d - 1)
        x_old_k = x[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        old_radius_square = 0
        for r in x:
           old_radius_square += r**2;
        new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
        if new_radius_square < 1.0:
            x[k] = x_new_k
            alpha = random.uniform(-1.0, 1.0)
            if new_radius_square + alpha**2 <1:
                n_hits += 1
    dict[d+1] = 2 * n_hits / float(n_trials)
print(dict)

VList = [];
for j in range(2, 200):
    V = 2;
    for i in range(2, j):
        V *= dict[i]
    VList.append(V)

pylab.yscale('log')
pylab.plot(range(3,201), VList)
a = [x * 1/200.0 for x in range(0, 200)]
b = [4*r**3 for r in a]
b = pylab.plot(a,b, color = 'red')
pylab.show()
    
# a = [x * 1/100.0 for x in range(0, 100)]
# b = [20*r**19 for r in a]
# b = pylab.plot(a,b, color = 'red')
# a = pylab.hist(rList, density = True)
# pylab.show()

# def V_sph(dim):
#     return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

# for d in range(1, 200):
#     print (d, V_sph(d), V_sph(d)/V_sph(d-1))