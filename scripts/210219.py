import numpy as np, pandas as pd
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# import file
file_to_use = "titration1"
data = np.genfromtxt("../raw_data/" + file_to_use + ".txt", skip_header=2)   #skips first 2 lines

volume = data[:,0]  #: is all rows, column 1
emf = data[:,1]
temperature = data[:,2]

#combine the array into a dict
titration = {
    "volume": volume,
    "emf": emf,
    "temperature": temperature,
    }
# Make a dataframe out of the dict
titration = pd.DataFrame(titration)

# Make a logical array / subset
L = ((volume >= 3) & (emf < 460)) | (volume < 1)
titration_L = titration[L]

# Working wiith dataframes
vol = titration['volume']     # same as titration.volume but more powerfull
# ^ access columns
titration['whatever'] = 15
titration['volume_squared'] = titration.volume ** 2
# ^ makes a new column. Not possible with the dot notation
vol_L = titration[L]['volume']
vol_L = titration['volume'][L]
vol_L = titration[L].volume
vol_L = titration.volume[L]
# ^ all do the exact same thing: take the volume column from the L subset

# Make a plot
fig, ax = plt.subplots(dpi=300)
ax.grid(alpha=0.3) #alpha is transparancy
# ax.scatter(volume,emf, s=35, c='xkcd:navy') #S = size of points, c= color, alpha = transparancy
sc_full = ax.scatter('volume','emf', data=titration, s=35, c='emf', cmap='plasma')
sc = ax.scatter('volume','emf', data=titration[L],
           s=35, c='emf') #c='emf' uses the color from the emf dataframe in the plot
plt.colorbar(sc)
plt.colorbar(sc_full)
#ax.scatter(volume[L],emf[L], s=35, c='xkcd:tangerine')
#ax.scatter(volume[25:],emf[25:], s=35, c='xkcd:orange', alpha=0.5)
ax.set_xlabel('volume / mL')
ax.set_ylabel('EMF / mV')


