import pandas as pd, numpy as np
from matplotlib import pyplot as plt
#import matplotlib.pypolt as plt # would also work

#import dataset
#ignore invalid data (-9999)
glodap = pd.read_csv(
    'C:/Users/dnalab/Desktop/mini tutorial/201009/GLODAPv2.2020_Indian_Ocean.csv',
    na_values=-9999)

#%% make a scatterplot tco2 / talk

#make an empty canvas, define resolution
#nrows = number of rows taken into account (default = 1)
fig, axs = plt.subplots(dpi=300, figsize=(5,6), nrows=2) #size width/height in inches

#add data, use the first axis
ax=axs[0]
#make a plot and put it on the empty canvas
#pandas-style
#glodap[glodap["depth"] <20].plot.scatter('tco2','talk', ax=ax, s=3) 
#matplotlib-style
scatter_pts = ax.scatter(
    "tco2",
    "talk",
    data=glodap[glodap["depth"] <20],
    s=3,
    c= "temperature",
    cmap= "plasma"
    )    
#add colorbar to first axis
cb = plt.colorbar(scatter_pts, ax=ax)
cb.set_label("temperature / °C")
#control figure settings
#Latex-style formatting between $..$   #$^{}$ superscript
ax.set_xlabel("DIC / μmol kg$^{-1}$")  
ax.set_ylabel("Alkalinity / μmol kg$^{-1}$")
#Set a grid, transparancy = alpha 
ax.grid(alpha=0.3)
#add text in the plot at a certain x-y position
#ax.text(1800, 2400, "(a)" )
#add text in the plot at a certain fraction of the plot (transform to fraction)
ax.text(0, 1.05, "(a)", transform=ax.transAxes)

#for the second axis===========================================================
#add data, use the second axis
ax=axs[1]
#make a plot and put it on the empty canvas 
scatter_pts = ax.scatter(
    "salinity",
    "temperature",
    data=glodap[glodap["depth"] <20],
    s="temperature",
    c= "latitude",
    cmap= "viridis"
    )    
#add colorbar to second axis
cb = plt.colorbar(scatter_pts, ax=ax)
cb.set_label("latitute / °N")
#control figure settings
#Latex-style formatting between $..$   #$^{}$ superscript
ax.set_xlabel("Salinity")  
ax.set_ylabel("Temperature / °C")
#Set a grid, transparancy = alpha 
ax.grid(alpha=0.3)
#add text in the plot at a certain fraction of the plot (transform to fraction)
ax.text(0, 1.05, "(b)", transform=ax.transAxes)
#mark selected values with ticks on the axis
ax.set_xticks(np.arange(25,50,2))
#make the x-axis within limits
ax.set_xlim(20,40)


#matplotlib magic to fix the layout of axes etc.
plt.tight_layout()
#allign labels from the two plots
fig.align_ylabels()
#save the figure, also possible as .pdf or other file type
plt.savefig("mpl_scatter.png")

#%%
