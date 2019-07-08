import numpy as np
from settings import *
import random

def add_linear(g):
    t1D = np.arange(t0,nSamples*dt,dt, dtype = np.float32)
    t = np.repeat(t1D,nOffsets)
    t.shape = (nSamples,nOffsets)

    """This function takes zeroed gathers and adds mutiple events to them"""
    maxOffset = minOffset + stepOffset*nOffsets
    for i in range(0, g.shape[0]):
        nEvent = random.randint(12,22)
        for j in range(nEvent):
            ampl = random.randint(80,120)/100.0
            dip = random.randint(30,60)
            evSample = random.randint(t0, nSamples)
            evTime = dt*evSample
            evTimeOffset = np.repeat(evTime, nOffsets)
            for k in range(nOffsets):
                offset = minOffset + stepOffset*k
                evTimeOffset[k] = evTimeOffset[k] + k*dip
            evTimeOffset.shape = (1,nOffsets)
            evTimeCurv = np.repeat(evTimeOffset,nSamples, axis = 0)
            phase = random.randint(0, 360)
            g[i,:,:] = g[i,:,:] + ampl*0.2*np.exp(-(t - evTimeCurv)**2 / (2 * 5.**2))
    #print(t[:,0])
    #print(evTimeCurv[:,22])
    return g
