# data manipulation
import pandas as pd
import numpy as np
from numpy import genfromtxt

# visualiation
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# dataset size
num_data = 20
width = 5 
cell_width = 1 

# Gaussian parameters for noise
mean = 0.0 
sigma = 0.1
plot =1

# Input:
Z_xyz = genfromtxt('data\Input.csv')
#print(Z_xyz.shape)

# modify input to decrete number
Iz_xyz = np.ceil(Z_xyz/cell_width) # round up to cell no: Iz_x, Iz_y, Iz_z
#np.savetxt("Input_cell.csv", Iz_xyz)

# generate the random noise
shape = Z_xyz.shape
noise = np.random.normal(mean, sigma, (shape[0], shape[1]))
# add noise to datasetInput
X_xyz = Z_xyz + noise
#np.savetxt("Output.csv", X_xyz)

# Output
Ix_xyz = np.ceil(X_xyz/cell_width) # round up to cell no: Ix_x, Ix_y, Ix_z
#np.savetxt("Output_cell.csv", Ix_xyz)

if(plot):
    # plot in 3D space - actual trace in green
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.title('Fig1. discrete trace info: Iz_x, Iz_y, Iz_z')
    # actual trace in green, cell center
    zline = (Iz_xyz[:,0]-0.5)
    xline = (Iz_xyz[:,1]-0.5)
    yline = (Iz_xyz[:,2]-0.5)
    ax.plot3D(xline, yline, zline, 'green')

    # plot in 3D space - actual trace in green
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.title('Fig1. discrete trace info: Iz_x, Iz_y, Iz_z')
    # actual trace in green, cell center
    zline = (Iz_xyz[:,0]-0.5)
    xline = (Iz_xyz[:,1]-0.5)
    yline = (Iz_xyz[:,2]-0.5)
    ax.plot3D(xline, yline, zline, 'green')

    plt.title('Fig2. discrete trace info: Ix_x, Ix_y, Ix_z')
    # actual trace in green, cell center
    zline = (Ix_xyz[:,0]-0.5)
    xline = (Ix_xyz[:,1]-0.5)
    yline = (Ix_xyz[:,2]-0.5)
    ax.plot3D(xline, yline, zline, 'red')
    
    
# 2. do we manually add fault outliers??
