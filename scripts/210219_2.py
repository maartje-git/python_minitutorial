import pandas as pd

#%% Import data as a DataFrame
glodap = pd.read_csv("raw_data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

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
