import numpy as np
from settings import *
import matplotlib.pyplot as plt
from plot_gathers import plot_gathers
from add_event import add_event
from add_noise import add_random_noise
from add_multiples import add_multiples
from add_linear import add_linear
from distort_signal import distort_signal
import random
from numpy import linalg as LA

random.seed(1)
np.random.seed(22223)
nGather = 2 # number of gathers to create
g = np.zeros((nGather, nSamples, nOffsets), dtype = np.float32)
add_event(g)
distort_signal(g)
# s = g.copy()
add_random_noise(g)
add_multiples(g)
add_linear(g)
y = plot_gathers(g[::1000],0,4000)

# print(LA.norm(g-s,axis=(1,2)))
# print(np.average(LA.norm(g-s,axis=(1,2))))
# np.save('test_gather',g)
# gLoaded = np.load('test_gather.npy')
# y = plot_gathers(gLoaded[::1000],0,4000)
