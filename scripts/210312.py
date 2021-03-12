import pandas as pd, numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift

# import glodap dataset
glodap = pd.read_csv("C:/Users/dnalab/Desktop/python_work/mini_tutorial/repository/python_minitutorial/raw_data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)
# na_value = -9999 ==> nan = not a number, will be skipped

#%% select staion
fvar = "tco2"
L = (glodap.cruise == 387) & (glodap.station == 11) & ~np.isnan(glodap[fvar])    # ~ is not

# extract x and y variables
x_values = glodap[fvar][L].to_numpy()                   
depth_values = glodap.depth[L].to_numpy()
# .to_numpy() turns it in a numpy array

# sort arrays
# depth_index = np.argsort(depth_values)
# x_valuess = x_values[depth_index]
# depth_values = depth_values[depth_index]

# # do a PCHIP interpolation
# # normally the variable would be on the y-axis, but in ocenaography depth is on the y-axis.
# # interpolator = interpolate.pchip(depth_values, x_values)
# # gives an error because it's not increasing because there are also equal x_values
# # average duplicate values
# depth_unique = np.unique(depth_values)
# x_unique = np.full_like(depth_unique, np.nan)
# for i in range(len(depth_unique)):
#     x_unique[i] = np.mean(x_values[depth_values == depth_unique[i]])
# # now interpolation on unique values should work    
# interpolator = interpolate.pchip(depth_unique, x_unique)
# depth_plotting = np.linspace(np.min(depth_values), 
#                              np.max(depth_values), num =1000)
# x_plotting = interpolator(depth_plotting)

# # clustering 
# # cluster close values together, so that the interpolation is smoother, without meaning the equal values
# # the values should be in a column.. depth is just an 1D array
# depth_values_v = np.vstack(depth_values)
# clustering = MeanShift(bandwidth=10).fit(depth_values_v) # clusters together withing 10m depth
# cluster_labels = clustering.labels_

# # average by cluster
# depth_clusters = clustering.cluster_centers_.ravel()
# # .ravel makes anything 1 dimensional
# x_clusters = np.full_like(depth_clusters, np.nan)
# for i in range(len(depth_clusters)):
#     x_clusters[i] = np.mean(x_values[cluster_labels == i])
    
# # sort arrays
# depth_index = np.argsort(depth_clusters)
# x_clusters = x_clusters[depth_index]
# depth_clusters = depth_clusters[depth_index]

# #Interpolation with clustered data
# interpolator = interpolate.pchip(depth_clusters, x_clusters)
# depth_plotting = np.linspace(np.min(depth_clusters), 
#                               np.max(depth_clusters), num =1000)
# x_plotting = interpolator(depth_plotting)

# make a clustering function out of it
def cluster_profile(depth_values, x_values, bandwidth=10):
    """Cluster depth profile data with MeanShift and Interpolate"""
    # clustering 
    # cluster close values together, so that the interpolation is smoother, without meaning the equal values
    # the values should be in a column.. depth is just an 1D array
    depth_values_v = np.vstack(depth_values)
    clustering = MeanShift(bandwidth=bandwidth).fit(depth_values_v) # clusters together withing 10m depth
    cluster_labels = clustering.labels_
    
    # average by cluster
    depth_clusters = clustering.cluster_centers_.ravel()
    # .ravel makes anything 1 dimensional
    x_clusters = np.full_like(depth_clusters, np.nan)
    for i in range(len(depth_clusters)):
        x_clusters[i] = np.mean(x_values[cluster_labels == i])
        
    # sort arrays
    depth_index = np.argsort(depth_clusters)
    x_clusters = x_clusters[depth_index]
    depth_clusters = depth_clusters[depth_index]
    
    #Interpolation with clustered data
    interpolator = interpolate.pchip(depth_clusters, x_clusters)
    depth_plotting = np.linspace(np.min(depth_clusters), 
                                  np.max(depth_clusters), num =1000)
    x_plotting = interpolator(depth_plotting)
    
    return depth_clusters, x_clusters, depth_plotting, x_plotting

#run the function
depth_clusters, x_clusters, depth_plotting, x_plotting = cluster_profile(
    depth_values, x_values, bandwidth=100)

#%% basic plotting
fig, ax = plt.subplots(dpi=300)
glodap[L].plot.scatter(fvar, "depth", ax=ax, s=50)
# glodap[L].plot("tco2", "depth", ax=ax, legend=False)  # draws a line between points
ax.scatter(x_clusters, depth_clusters, c="purple", s=10)
ax.plot(x_plotting, depth_plotting, c="red")            # interpolated line
ax.set_ylim([0, 1250])
ax.invert_yaxis()                                       # ax.set_ylim([1500, 0]) would invert the axis

