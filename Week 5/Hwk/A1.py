import random, math, pylab

def psi_0_sq(x):
    return ((1/math.pi**(1/4))* math.exp( - x**2 / 2))**2
    
x = 0.0
delta = 0.5
pyList = []
for k in range(100000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  \
         psi_0_sq(x_new) / psi_0_sq(x): 
        x = x_new
        # print(x)
    pyList.append(x)

pylab.hist(pyList, density = True)
xVal = [-3 + x*6/100 for x in range(100)]
yVal = [psi_0_sq(x) for x in xVal]
pylab.plot(xVal,yVal,color = 'red')
pylab.xlabel("x Value")
pylab.ylabel("Probability")
pylab.title('Graph for both Monte-Carlo and Psi Methods')
pylab.legend()
pylab.show()
