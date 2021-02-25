import numpy as np, pandas as pd
from matplotlib import pyplot as plt
import cmocean #oceanography colormaps
from scipy import interpolate, stats
import cmocean

#%% Import data as a DataFrame
glodap = pd.read_csv("python_minitutorial/raw_data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% Make a plot
L = glodap.depth < 20
glodap[L].plot.scatter(
    "longitude", 
    "latitude", 
    c="temperature", cmap='viridis'
    )

# HOMEWORK
# with some spreadsheet file
# - import with pandas
# - make a scatterplot of something interesting
# - using a logical to subset of the df
# EXTENSION
# - use interpolation to join scatter points

#%% HOMEWORK
# Import data
bs = pd.read_csv(
    "python_minitutorial/raw_data/NIOZ102_16S_blackSea.txt",
    sep="\t"
    )

#%%
# Make a scatterplot
bs.plot.scatter(
    "salinity",
    "depth",
    c="temperature", cmap='RdBu_r'
   )
plt.gca().invert_yaxis()
#%%
# Combine the array into a dict
sal = {
    "depth": bs.depth,
    "salinity": bs.salinity,
    "temperature": bs.temperature,
    "oxygen": bs.oxygen,
    }
# Make a dataframe out of the dict
sal = pd.DataFrame(sal)

# Make a subset
S = ((bs.depth > 50) & (bs.depth < 1500))
sal_S = sal[S]

# Make a scatterplot
sal[S].plot.scatter(
    "salinity",
    "depth",
    c="temperature", cmap='RdBu_r'
   )
plt.gca().invert_yaxis()

#%% Make a plot
fig, ax = plt.subplots(dpi=300)
ax.grid(alpha=0.3)
sc = ax.scatter(
    'salinity', 'depth',
    data=sal[S],
    s=35, c='oxygen', cmap='cmo.oxy')
cbar = plt.colorbar(sc)
cbar.set_label('oxygen (mg/L)')
plt.gca().invert_yaxis()                #invert axis for depth
ax.set_xlabel('salinity (ppt)')
ax.set_ylabel('depth (m)')
ax.set_title('salinity')

#%% make another plot
fig, ax = plt.subplots(dpi=300)
ax.grid(alpha=0.3)
sc = salinity = ax.scatter(
    'DIC', 'NH4',
    data=bs,
    s=35, c='temperature', cmap='cmo.thermal')
cbar = plt.colorbar(sc)
cbar.set_label('temperature (˚C)')
ax.set_xlabel('DIC (µmol $kg^{-1}$)')
ax.set_ylabel('$NH4^{+}$ (µmol $L^{-1})$)')
ax.set_title('ammonium')
# Save figure to file
plt.savefig("python_minitutorial/output/210219_BlackSea_ammonium.png")

#%% interpolation
#interpolate the data
interp_nearest = interpolate.interp1d(bs.salinity, bs.depth, kind='nearest')
interp_spline = interpolate.UnivariateSpline(bs.salinity, bs.depth, s=1000) 
# Linear regression
slope, intercept, rv, pv, se = stats.linregress(bs.salinity, bs.depth)

# Interpolate data points between the actual data points (500 between min and max)
salinity_interp = np.linspace(np.min(bs.salinity), np.max(bs.salinity), num=500)

# Apply interpolation
depth_nearest = interp_nearest(salinity_interp)
depth_spline = interp_spline(salinity_interp)

# Make a plot
fig, ax = plt.subplots(dpi=300)
ax.grid(alpha=0.3)
sc = ax.scatter(
    'salinity', 'depth',
    data=sal[S],
    s=35, 
    c='oxygen', cmap='cmo.oxy',
    zorder=10
    )
ax.plot(
        'salinity', 'depth', 
        data=sal[S], 
        label="Direct plot")
ax.plot(
        salinity_interp,
        depth_nearest,
        label="interp1d nearest"
        )
ax.plot(
        salinity_interp,
        intercept + slope * salinity_interp,
        label='Linear regression',
        linestyle="--"
        )
ax.plot(
        salinity_interp,
        depth_spline,
        label="spline"
        )
cbar = plt.colorbar(sc)
cbar.set_label('oxygen (mg $L^{-1})$')
plt.gca().invert_yaxis()                #invert axis for depth
ax.set_xlabel('salinity (ppt)')
ax.set_ylabel('depth (m)')
plt.ylim(1100,0)
ax.set_title('salinity')
ax.legend() 

# Save figure to file
plt.savefig("python_minitutorial/output/210219_BlackSea_salinity_depth.png")

#%% make another plot with interpolation
#interpolate the data
interp_nearest = interpolate.interp1d(bs.DIC, bs.NH4, kind='nearest')
# Linear regression
slope, intercept, rv, pv, se = stats.linregress(bs.DIC, bs.NH4)
# Interpolate data points between the actual data points (500 between min and max)
DIC_interp = np.linspace(np.min(bs.DIC), np.max(bs.DIC), num=500)
# Apply interpolation
NH4_nearest = interp_nearest(DIC_interp)

# plot
fig, ax = plt.subplots(dpi=300)
ax.grid(alpha=0.3)
sc = salinity = ax.scatter(
    'DIC', 'NH4',
    data=bs,
    s=35, c='temperature', cmap='cmo.thermal',
    zorder=10
    )
ax.plot(
        'DIC', 'NH4',
        data=bs,
        label="Direct plot",
        )
ax.plot(
        DIC_interp,
        intercept + slope * DIC_interp,
        label='Linear regression',
        linestyle="--"
        )
ax.plot(
        DIC_interp,
        NH4_nearest,
        label="interp1d nearest"
        )
cbar = plt.colorbar(sc)
cbar.set_label('temperature (˚C)')
ax.set_xlabel('DIC (µmol $kg^{-1}$)')
ax.set_ylabel('$NH4^{+}$ (µmol $L^{-1})$)')
ax.set_title('ammonium')
ax.legend()
# Save figure to file
plt.savefig("python_minitutorial/output/210219_BlackSea_ammonium_interpol.png")