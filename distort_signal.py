import numpy as np
from settings import *
from trace_shift import trace_shift
import random

def distort_signal(g):
    """This function takes gathers and adds slight distortion the events on them"""
    for i in range(0,g.shape[0]):
        for j in range(0,g.shape[2]):
                g[i,:,j] = (random.randint(9,11)/10.0)*trace_shift(g[i,:,j], random.randint(0,4))

    return g
