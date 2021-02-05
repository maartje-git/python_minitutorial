import xarray as xr

# import dataset
gebco = xr.open_dataset("C:/Users/dnalab/Desktop/mini tutorial/201106/gebco_2020_n50.9_s41.7_w-12.7_e-0.1.nc")

#change axis label
gebco.elevation.attrs["long_name"] = "Elevation"

#%%plot data
gebco.elevation.plot()

#%% select a single grid row and plot
#plots longitude value closest to -8
gebco.elevation.sel(lon=-8, method='nearest').plot()

#%% Import satelite data directly from online
oc = xr.open_dataset("https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/2020/0101/AQUA_MODIS.20200101.L3m.DAY.SST.sst.9km.nc")

#%% Coarsen the data and then plot
oc.sst.coarsen(lat=5, lon=7, boundary="trim").mean().plot(vmin=0, vmax=30, cmap="magma_r")

#%% select a subset of the data
#get latituted in northern hemisphere
northern_hem = oc.lat[oc.lat > 0]
lon_range = oc.lon[(oc.lon > -100) & (oc.lon < 0 )]

#plot it
oc.sst.sel(lat=northern_hem, lon=lon_range, method="nearest").plot(vmin=0, vmax=30, cmap="magma_r")

#%%Interpolate gaps 
oc.sst.coarsen(lat=5, lon=5, boundary="trim").mean().interpolate_na(dim="lon").plot()

#%%nicer way to organize long lines
(
 oc.sst
 .coarsen(lat=5, lon=5, boundary="trim").mean()
 .interpolate_na(dim="lon")
 .plot(vmin=0, vmax=30, cmap="magma")
 )

#%% 
(
 oc.sst
 .coarsen(lat=5, lon=5, boundary="trim").mean()
 .interpolate_na(dim="lon")
 .plot(vmin=0, vmax=30, cmap="magma")
 )

#%% black sea
#get latituted and longitude range for area of interest
lat_range = oc.lat[(oc.lat > 0) & (oc.lat < 150)]
lon_range = oc.lon[(oc.lon > 0) & (oc.lon < 142)]

#plot it
oc.sst.sel(lat=lat_range, lon=lon_range, method="nearest").plot(vmin=0, vmax=30, cmap="magma")



