import numpy as np
import nbinteract as nbi

def normal(mean, sd):
    '''Returns 1000 points drawn at random fron N(mean, sd)'''
    return np.random.normal(mean, sd, 1000)

# Pass in the `normal` function and let user change mean and sd.
# Whenever the user interacts with the sliders, the `normal` function
# is called and the returned data are plotted.
nbi.hist(normal, mean=(0, 10), sd=(0, 2.0))


rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=300)
averages = np.cumsum(rolls) / np.arange(1, 301)

def x_vals(num_rolls):
    return range(num_rolls)

# The function to generate y-values gets called with the
# x-values as its first argument.
def y_vals(xs):
    return averages[:len(xs)]

nbi.line(x_vals, y_vals, num_rolls=(1, 300))
