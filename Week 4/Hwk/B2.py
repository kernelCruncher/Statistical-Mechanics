import random, math, pylab

d = 4
x = [0] * d
delta = 0.05
n_trials = 400000
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
    rList.append(math.sqrt(x[0]**2+x[1]**2+x[2]**2+x[3]**2))   
print (2 * n_hits / float(n_trials))

# a = [x * 1/100.0 for x in range(0, 100)]
# b = [20*r**19 for r in a]
# b = pylab.plot(a,b, color = 'red')
# a = pylab.hist(rList, density = True)
# pylab.show()

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

for d in range(1, 200):
    print (d, V_sph(d), V_sph(d)/V_sph(d-1))