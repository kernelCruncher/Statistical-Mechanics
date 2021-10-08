import random

def markov_disks_box(sigma, L):
    delta = 0.1
    "We randomly choose a disk and move it a little."
    randomNumber = random.choice([0,1,2,3])
    a = L[randomNumber]
    "The disk is moved a little:"
    b = (a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta))
    "We check that the new movement is valid"
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 4.0 * sigma ** 2):
        L[randomNumber] = b;
    return L

sigma = 0.15
del_xy = 0.05
number_of_runs = 10**7
conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}
L = [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)]

"We compute the n_runs of different configurations"
for run in range(number_of_runs):
    L= markov_disks_box(sigma, L)
    for conf in configurations:
        condition_hit = True
        "This is checking if the configurations, i.e. conf(a), conf(b), conf(c), are sufficientky close to the x_vec"
        for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in L) < del_xy
            condition_hit *= condition_b
        if condition_hit:
            hits[conf] += 1

for conf in configurations:
    print (conf, hits[conf])#