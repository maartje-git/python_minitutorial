from cartopy import crs as ccrs, feature as cfeature
from matplotlib import pyplot as plt
import pandas as pd
import xarray as xr
import numpy as np


# Import data
rws = pd.read_excel(
    "../raw_data/RWS-NIOZ North Sea data v6-1 for SDG14-3-1.xlsx", na_values=-999,
)
gebco = xr.open_dataset("../raw_data/gebco_2020_noordzee.nc")

#%%Do per-station analysis
def per_station(station):
    return pd.Series({
        "latitude": station.LATITUDE.mean(),
        "longitude": station.LONGITUDE.mean(),
        "dic_count": np.sum(~np.isnan(station.dic)),
        
        })

#test function
walcrn2 = rws[rws.station == "WALCRN@"]
station_test = per_station(rws)
                
stations = rws.groupby("station").apply(per_station)        

#%% Initialise figure
#make white background
fig = plt.figure(dpi=300)
#add figure
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

#cartopy projection list (google) for more options

# Quick visualisation of the coastlines
# ax.coastlines()

# Add more detailed features from NaturalEarthData.com
#10m = high resolution
#110M = low data
ax.add_feature(
    cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k",
)
ax.add_feature(
    cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor="w",
)
ax.add_feature(
    cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k",
)

# Scatter the data
#zorder puts scatter on top of map
ax.scatter(
    "LONGITUDE",
    "LATITUDE",
    data=rws, 
    transform=ccrs.PlateCarree(), 
    zorder=10)
#add (a) on the graph
ax.text(0, 1.05, "(a)", transform=ax.transAxes)
# transform kwarg sets what format the x and y numbers are in, not the projection that
# they are going to

#plot 
gplot = (
    gebco.elevation
    .coarsen(lon=5, lat=5, boundary="trim").mean()
    .plot(
        add_colorbar=False,
        ax=ax,
        cmap="gray",
        transform=ccrs.PlateCarree(),
        vmin=-200,
        vmax=0,
        )
)
#add color bar manually, so you can adjust it
gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth / m")
gcbar.set_ticks(np.arange(-200, 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())


# Plot settings
# ax.set_global()
ax.set_extent((0, 8, 50, 57))  # west, east, south, north limits
ax.gridlines(alpha=0.3)

