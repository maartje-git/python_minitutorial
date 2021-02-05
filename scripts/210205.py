import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# import file
file_to_use = "titration1"
data = np.genfromtxt("../raw_data/" + file_to_use + ".txt", skip_header=2)   #skips first 2 lines

volume = data[:,0]  #: is all rows, column 1
emf = data[:,1]
temperature = data[:,2]

#Other calculations
emf_sqrt = np.sqrt(emf)
emf_log = np.log(emf)
emf_log10 = np.log10(emf)

#Summary statistics
emf_mean = np.mean(emf)
emf_median = np.median(emf)
emf_std = np.std(emf)

# Make a plot
fig, ax = plt.subplots(dpi=300)
ax.scatter(volume,emf, s=35, c='xkcd:periwinkle') #S = size of points, c= color, 
ax.set_xlabel('volume / mL')
ax.set_ylabel('EMF / mV')
ax.grid(alpha=0.3) #alpha is transparancy

#Save figure to file
plt.savefig("../output/210205_" + file_to_use + "_VOLUMEvsEMF.png")

