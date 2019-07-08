import numpy as np
from settings import *
import random

def add_random_noise(g):
    """This function takes gathers and adds noise to them"""
    a = (np.random.normal(0,1,(g.shape[0],g.shape[1],g.shape[2]))).astype(np.float32)
    g[:,:,:] = g[:,:,:] + 0.01*random.randint(1,5)*a[:,:,:] # random noise added
    return g
