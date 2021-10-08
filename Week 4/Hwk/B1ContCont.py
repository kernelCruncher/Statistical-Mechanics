import random, math, pylab

d = 10
x = [0] * d
delta = 0.1
n_trials = 40000
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
    rList.append(math.sqrt(x[0]**2+x[1]**2+x[2]**2+x[3]**2+x[4]**2+x[5]**2+x[6]**2+x[7]**2+x[8]**2+x[9]**2))    
#         alpha = random.uniform(-1.0, 1.0)
#     if x**2 + y**2 + z**2 + alpha**2< 1.0: n_hits += 1
# print (2.0 * n_hits / float(n_trials))

a = [x * 1/100.0 for x in range(0, 100)]
b = [20*r**19 for r in a]
print(b)
b = pylab.plot(a,b, color = 'red')
a = pylab.hist(rList, density = True)
pylab.show()