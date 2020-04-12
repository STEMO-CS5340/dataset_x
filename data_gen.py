# data manipulation
import pandas as pd
import numpy as np
from numpy import genfromtxt

# visualiation
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# generate input
# dataset size
num_data = 20
width = 5 
cell_width = 1 

# Input: 
Z_xyz = width*np.random.random_sample((num_data, 3)) # actual data Z_x, Z_y, Z_z
np.savetxt("data\Input.csv", Z_xyz)
