import numpy as np
from settings import *

# t is an input trace
# shift is a shift in samples

def trace_shift(t, shift):
    """This function takes a trace and shifts it, padding with zeroes"""
    shift = -shift # following Insight
    tShifted = 0 * t
    for i in range(0,t.size):
        if (i+shift)<t.size and (i+shift)>0:
            tShifted[i] = t[i+shift]

    return tShifted
