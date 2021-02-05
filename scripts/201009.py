import pandas as pd

#import dataset
#ignore invalid data (-9999)
data = pd.read_csv(
    '../raw_data/GLODAPv2.2020_Indian_Ocean.csv',
    na_values=-9999)
surface = data['depth'] < 20

#add a column to the table
data['ts'] = data['temperature'] * data['salinity']


#import a .tab file
# change the sep(erator) from , (default) to a tab
# skip the first 55 row, because it has irrelevant data
cocco = pd.read_csv(
    '../raw_data/Poulton-etal_2018.tab',
    sep='\t', skiprows=55)


#Make code cells so that you do not have to 
#import the big data set everytime you run the script
#%% make a plot
#s = size of markers
#c = color (google xkcd names)
#alpha = transparancy
data.plot.scatter('tco2', 'talk', s=2, c='xkcd:eggplant', alpha = 0.05)
#%%
#color shades c = 'column name'
#colormap = cmap google matplotlib colormaps _r = reversed colormap
data.plot.scatter('tco2', 'talk', s=2, c='salinity', alpha = 0.5, cmap='viridis_r')
#%% map
#plot.scatter('x-axis', 'y-axis')
data[surface].plot.scatter('longitude', 'latitude', s=2, c='temperature', cmap='magma')

#%% transect
#plot.scatter('x-axis', 'y-axis')
data[surface].plot.scatter('latitude', 'depth', s=2, c='temperature', cmap='magma')
data.plot.scatter('tco2', 'ts', s=2, c='temperature', cmap='magma')

#%% make a histogram for a specific column
cocco['Coccolith [#/ml]'].plot.hist()

#%%subset columns and rows with .loc['row', 'column']
cocco.loc[cocco['PI'] == 'Daniels' , 'Coccolith [#/ml]'].plot.hist()

#%% rename columns
#Make a renaming dictionary
mapper = {'Coccolith [#/ml]' : 'coccolith_count',
          'E. huxleyi [#/ml]' : 'ehux_count'}

cocco = cocco.rename(columns=mapper)
cocco.loc[cocco['PI'] == 'Daniels' , 'coccolith_count'].plot.hist()

#Save with new column names
cocco.to_csv('../raw_data//Poulton_v2.csv')

#%% read an excel file
#tell which column is the index (otherwise it will number it from 1 to ...)
#let it recognize dates with parse_dates
msl = pd.read_excel(
    '../raw_data/csiro_alt_gmsl_yr_2015.xlsx',
    index_col=0, parse_dates=True)
msl.plot()
