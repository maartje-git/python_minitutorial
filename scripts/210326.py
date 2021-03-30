import numpy as np, pandas as pd
from matplotlib import pyplot as plt
from numba import jit
from scipy import interpolate

# set-up model time variables
t_start = 0
t_end = 365.25 * 5                     # in days, 5 years
t_step = 1/24                           # per hour
days = np.arange(t_start, t_end, t_step)

# define model parameters
dic_increase_rate = 0.1 # per day
k_mixing = 0.01         # per day
# ncp_rate = np.full_like(days, 1.5)
ncp_rate = np.sin(days * 2 * np.pi / 365.25) + 1

# import data
chl = pd.read_csv('raw_data/walcrn70_chlorophyll.csv')
chl = chl[~np.isnan(chl.chlorophyll)]
ncp_rate = interpolate.pchip(chl.days.to_numpy(),
                             chl.chlorophyll.to_numpy()
                             )(days)

@jit    # decorator, makes the model much more efficient
def model():
    # pre_allocate variables
    dic_surf = np.full_like(days, np.nan)   # makes an empty array
    dic_deep = np.full_like(days, np.nan)
    
    # assign initial values
    dic_surf[0] = 2000.0
    dic_deep[0] = 2200.0              
    # dic_deep = dic_surf makes it the same variable
    # copy makes it a new variable
    
    # run the model
    # dic_surf[1] = dic_surf[0] + dic_increase_rate * t_step
    # dic_surf[2] = dic_surf[1] + dic_increase_rate * t_step
    # dic_surf[3] = dic_surf[2] + dic_increase_rate * t_step
    
    # in a loop
    for i in range(len(days) - 1):
        
        # calculate changes due to different processes
        dic_mixing_s2d = k_mixing * (dic_surf[i] - dic_deep[i])
        dic_ncp = ncp_rate[i]
        
        # Apply changes to modelled variables
        dic_surf[i + 1] = dic_surf[i] + ( 
            dic_increase_rate 
            - dic_mixing_s2d
            - dic_ncp
            ) * t_step
        
        dic_deep[i + 1] = dic_deep[i] + (
            dic_mixing_s2d
            + dic_ncp
            ) * t_step
    
    return dic_surf, dic_deep

dic_surf, dic_deep = model()

#%% visualize what we did
fig, axs = plt.subplots(nrows=2, dpi=300)
ax = axs[0]
ax.plot(days, dic_surf, label = "surface")
ax.plot(days, dic_deep, label = "Deep")
ax.legend()
ax.set_xlabel("Days")
ax.set_ylabel("DIC")

ax = axs[1]
ax.plot(days, ncp_rate)
ax.set_xlabel("Days")
ax.set_ylabel("NCP")

plt.tight_layout()


