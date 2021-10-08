import random, math, pylab

def psi_n_square(x, n):
    if n == -1:
        return 0.0
    else:
        psi = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
        psi.append(math.sqrt(2.0) * x * psi[0])
        for k in range(2, n + 1):
            psi.append(math.sqrt(2.0 / k) * x * psi[k - 1] -
                       math.sqrt((k - 1.0) / k) * psi[k - 2])
        return psi[n] ** 2
def En(n):
    return n + 1/2;
    
def particle_position(beta): 
    x = 0.0
    delta = 0.5
    pyList = []
    n= 0  
    for k in range(100000):
        x_new = x + random.uniform(-delta, delta)
        if random.uniform(0.0, 1.0) <  \
             psi_n_square(x_new, n) / psi_n_square(x, n): 
            x = x_new
        n_new = random.choice([n-1, n+1])
        if random.uniform(0.0, 1.0) <  \
             psi_n_square(x, n_new) / psi_n_square(x, n) * math.exp(-beta*(En(n_new)-En(n))): 
            n = n_new
        pyList.append(x)
    return pyList

def quant_prob(x, beta):
    return math.sqrt(math.tanh(beta/2) / math.pi)* math.exp(-(x**2) * math.tanh(beta/2) )
def pi_class(x, beta):
    return math.sqrt(beta/ (2 * math.pi)) * math.exp(- beta * x**2/ 2)

x_input = [-8 + 16*x/100 for x in range(100)];
beta = 5
pylab.hist(particle_position(beta), density = True, label = f"Beta ={beta}")
pylab.plot(x_input, [quant_prob(x, beta) for x in x_input], label = "Quantum Probability" )
pylab.plot(x_input, [pi_class(x, beta) for x in x_input], label = "Classic Probability" )
pylab.legend()
pylab.show()
# pylab.hist(particle_position(1), density = True, label = "Beta = 1")
# pylab.hist(particle_position(5), density = True, label = "Beta = 5")




# xVal = [-3 + x*6/100 for x in range(100)]
# yVal = [psi_0_sq(x) for x in xVal]
# pylab.plot(xVal,yVal,color = 'red')
# pylab.xlabel("x Value")
# pylab.ylabel("Probability")
# pylab.title('Graph for both Monte-Carlo and Psi Methods')
# pylab.legend()
