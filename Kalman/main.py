import math

measurements = [ 5.,6., 7., 9., 10.]
motion = [1.,1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.


def f(mu,sigma2, x):
    return (1/math.sqrt(2*math.pi*sigma2)*math.exp(-0.5*((x-mu)**2)/sigma2))



def update(mean1, var1, mean2, var2):
    new_mean = (1/(var1 + var2)) * ( (var2 * mean1) + (var1 * mean2))
    new_var = 1/(1/var1 + 1/var2)

    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    return [ (mean1 + mean2), (var1 + var2)]



for i in range(len(measurements)):
    #update
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    print [mu, sig]
    #predict
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    print [mu, sig]
    
    
