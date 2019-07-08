import numpy as np
from settings import *
import matplotlib.pyplot as plt

# g.shape would return x,y,z where x is a gather number
# y is a number of time samples (every 2 ms)
# z is a number of offsets.
# For example x is 3, y is 2000, z is 24

def plot_gathers(g,ymin=1000, ymax=1550):
    # scaleMax = scale*np.amax(np.absolute(g))
    """This function takes a numpy array and plots it as seismic gathers"""
    nSubPlots = g.shape[0] # number of gather to be plotted
    fig = plt.figure()
    for i in range(nSubPlots):
        plt.subplot(1,nSubPlots,i+1)
        #plt.imshow(g[i],origin='upper',interpolation='bicubic',cmap='Greys', vmin = -scaleMax, vmax = scaleMax)
        for j in range(1, nOffsets+1):
            plt.plot(j + g[i,:,j-1],range(t0,nSamples),'k-')#, origin='upper')
            plt.fill_betweenx(range(t0,nSamples),j,j + g[i,:,j-1],where=(j + g[i,:,j-1]>j),color='k')
            ax = plt.gca() #you first need to get the axis handle
        ax.set_aspect(0.02) #sets the height to width ratio to 1.5.
        ax.xaxis.set_ticks_position('top')
        plt.title(f'Gather {i+1}', y=1.08)
        plt.ylabel('time, ms')
        plt.xlabel('offset, meters')
        plt.xticks(range(1,nOffsets+1,5),range(minOffset,minOffset + 5*nOffsets*stepOffset, 5*stepOffset))
        plt.yticks(range(t0,nSamples,250),range(t0,nSamples*dt,250*dt))
        ax.set_ylim([ymax/dt,ymin/dt])
        #c = plt.colorbar(fraction=0.046, pad=0.04)
        #c.set_ticks([-scaleMax,2*scaleMax,scaleMax])

    plt.show()
    return None
