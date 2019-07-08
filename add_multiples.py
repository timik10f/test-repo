import numpy as np
from settings import *
import random

def add_multiples(g):
    t1D = np.arange(t0,nSamples*dt,dt, dtype = np.float32)
    t = np.repeat(t1D,nOffsets)
    t.shape = (nSamples,nOffsets)

    """This function takes zeroed gathers and adds mutiple events to them"""
    maxOffset = minOffset + stepOffset*nOffsets
    for i in range(0, g.shape[0]):
        nEvent = random.randint(5,13)
        for j in range(nEvent):
            ampl = random.randint(80,120)/100.0
            curv = random.randint(350,650)
            evSample = random.randint(t0, nSamples)
            evTime = dt*evSample
            evTimeOffset = np.repeat(evTime, nOffsets)
            for k in range(nOffsets):
                offset = minOffset + stepOffset*k
                evTimeOffset[k] = evTimeOffset[k] + curv*np.power(1 + np.power(1.0*offset/maxOffset, 2.0),0.5)
            evTimeOffset.shape = (1,nOffsets)
            evTimeCurv = np.repeat(evTimeOffset,nSamples, axis = 0)
            phase = random.randint(0, 360)
            g[i,:,:] = g[i,:,:] + ampl*0.2*np.sin(t/2.+ phase)*np.exp(-(t - evTimeCurv)**2 / (2 * 5.**2))
    #print(t[:,0])
    #print(evTimeCurv[:,22])
    return g
