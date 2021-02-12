import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from scipy import interpolate, stats


# import file
file_to_use = "titration2"
data = np.genfromtxt("C:/Users/dnalab/Desktop/python_work/mini_tutorial/repository/python_minitutorial/raw_data/" + file_to_use + ".txt", skip_header=2)   #skips first 2 lines

volume = data[::3,0]           # takes every third value
emf = data[::3,1]
temperature = data[::3,2]      

# Interpolate the data
interp_linear = interpolate.interp1d(volume, emf, kind='linear')   #doesn't draw it in the plot yet
interp_nearest = interpolate.interp1d(volume, emf, kind= 'nearest')
interp_cubic = interpolate.interp1d(volume, emf, kind= 'cubic')
interp_pchip = interpolate.PchipInterpolator(volume, emf)
interp_spline = interpolate.UnivariateSpline(volume, emf, s=1000)   # higher s makes it smoother

# Linear regression
slope, intercept, rv, pv, se = stats.linregress(volume, emf)

# Interpolate data points between the actual data points (500 between min and max)
volume_interp = np.linspace(np.min(volume), np.max(volume), num=500)

# Apply interpolation
emf_linear = interp_linear(volume_interp)
emf_nearest = interp_nearest(volume_interp)
emf_cubic = interp_cubic(volume_interp)
emf_pchip = interp_pchip(volume_interp)
emf_spline = interp_spline(volume_interp)

# Make a plot
fig, ax = plt.subplots(dpi=300)
ax.scatter(volume,emf, s=35, c='xkcd:blue', zorder=10)    #S = size of points, c= color, zorder = order of drawing 
ax.plot(volume,emf, label="Direct plot")            # adds the line
ax.plot(volume_interp, emf_linear, label="interp1d linear", linestyle="--") # adds the interpolated line
ax.plot(volume_interp, emf_nearest, label="interp1d nearest")
ax.plot(volume_interp, emf_cubic, label="interp1d cubic")
ax.plot(volume_interp, emf_pchip, label="pchip")
ax.plot(volume_interp, intercept + slope * volume_interp, label='Linear regression')
ax.plot(volume_interp, emf_spline, label="spline")
ax.set_xlabel('volume / mL')
ax.set_ylabel('EMF / mV')
ax.grid(alpha=0.3)                                  #alpha is transparancy
ax.legend()                                         #adds a legend




#Save figure to file
plt.savefig("../output/210212_" + file_to_use + "_VOLUMEvsEMF.png")