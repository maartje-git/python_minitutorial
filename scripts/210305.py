import pandas as pd, numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt

# import glodap dataset
glodap = pd.read_csv("Documents/python_minitutorial/raw_data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% select staion
fvar = "tco2"
L = (glodap.cruise == 387) & (glodap.station == 11) & ~np.isnan(glodap[fvar])    # ~ is not

x_values = glodap[fvar][L].to_numpy()
depth_values = glodap.depth[L].to_numpy()

# sort arrays
depth_index = np.argsort(depth_values)
x_values = x_values[depth_index]
depth_values = depth_values[depth_index]

# do a PCHIP interpolation
# normally the variable would be on the y-axis, but in ocenaography depth is on the y-axis.
# interpolator = interpolate.pchip(depth_values, x_values)

# basic plotting
fig, ax = plt.subplots(dpi=300)
glodap[L].plot.scatter("tco2", "depth", ax=ax)
glodap[L].plot("tco2", "depth", ax=ax, legend=False)          # draws a line between points
ax.set_ylim([0, 1500])
ax.invert_yaxis()                               # ax.set_ylim([1500, 0]) would do the same
