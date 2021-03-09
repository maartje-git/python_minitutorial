import pandas as pd
from matplotlib import pyplot as plt

# import dataset
tm = pd.read_csv("raw_data/TM_Med.csv")

# rename depth (m) column. 
# Spaces and brackets are not usable outside strings
# rename the sample column. 
# Sample is a python methods so that might be confusing.
tm = tm.rename(columns={"depth (m)":"depth", "sample":"sample_name"})    
# returns a copy of the dataframe, doesn't change the first dataframe. 
# tm = at the start overwrites the first dataframe
# tm.rename(columns={"depth (m)":"depth"}, inplace=True)
# Does the same thing, but immediately replaces it in the first dataframe
# rename things in code, not manually in the data. Because next time you will 
# get similar data and you'll have to do all the modifications again.

# extract station and bottle number from sample name, first for 1 sample
# # Devide sample name by station and bottle number
# # Try to avoid putting multiple pieces of info in 1 column
# # First pick out one row
# tm_row = tm.loc[43]
# # .loc tells python that you are looking for the index numbers
# sname = tm_row.sample_name
# # split the sname string
# sname_split = sname.split()   # default separator is space
# # or in one go
# # sname_split = tm_row.sample_name.split()
# # get the stationnumber 
# station = int(sname_split[1])   # make an integer out of the string

# extract station number in a function
def get_station(tm_row):
    sname_split = tm_row.sample_name.split()
    station = int(sname_split[1])
    return station

# extract bottle number in a function
def get_bottle(tm_row):
    sname_split = tm_row.sample_name.split()
    bottle = int(sname_split[2])
    return bottle

# apply the function to the table
# make a new column in the data frame with this data
tm["station"] = tm.apply(get_station, axis=1)   # default axis=0 uses columns, we want rows=1
tm["bottle"] = tm.apply(get_bottle, axis=1) 

fvar = "Y89(LR)"
fstation = 1

# get all unique station numbers
stations = tm.station.unique()

# get the different variables (all end with (LR) or (MR)))
# get all column names
fvars = tm.columns
# check which ones end with (LR) or (MR)
L = fvars.str.endswith("(LR)") | fvars.str.endswith("(MR)")
# select the ones where (LR) or (MR) is TRUE
fvars = fvars[L]


#%%
# loop through all variables
for fvar in fvars:

    # make a loop through all stations
    for fstation in tm.station.unique():
        
        # make a plot for one station
        fig, ax = plt.subplots(dpi=300, figsize=(4,6))  #figsize in inches
        
        tm[tm.station == fstation].plot.scatter(fvar, "depth", ax=ax)
        ax.invert_yaxis()
        ax.set_ylabel("Depth / m")
        ax.grid(alpha=0.3)
        ax.set_title("station " + str(fstation) + " " + fvar)
        
        # to make sure everything is visible on the plot always put this at the end
        plt.tight_layout()
        
        # then at the very very last save the figure
        plt.savefig("C:/Users/dnalab/Desktop/python_work/mini_tutorial/repository/python_minitutorial/output/210226/depth_" + fvar + "_station" + str(fstation) + ".png")
        
        # to force show in the plots window
        plt.show()