import math, numpy, pylab

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# Harmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_harmonic_trotter(grid, beta):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * 0.5 * (x ** 2 + xp ** 2)) \
                         for x in grid] for xp in grid])

x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-int((nx - 1) / 2), int(nx / 2 + 1))]
beta_tmp = 2.0 ** (-5)                   # initial value of beta (power of 2)
beta     = 2.0 ** 2                     # actual value of beta (power of 2)
rho = rho_harmonic_trotter(x, beta_tmp)  # density matrix at initial beta
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    print ('beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp))
Z = sum(rho[j, j] for j in range(nx)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx)]
f = open('data_harm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
for j in range(nx):
    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
f.close()

beta = 4
def quant_prob(x, beta):
    return math.sqrt(math.tanh(beta/2) / math.pi)* math.exp(-(x**2) * math.tanh(beta/2) )
x_input = [-1 + 2*x/100 for x in range(100)];
pylab.hist(pi_of_x, density = True, label = "Pi(x)")
pylab.plot(x_input, [quant_prob(x, beta) for x in x_input], label = "Quantum Probability" )
pylab.legend()
pylab.show()
