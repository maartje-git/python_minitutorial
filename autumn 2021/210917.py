# Import and plot .csv
import pandas as pd
import numpy as np
import re #to be able to use regular expressions

#Import lat/lon/station info (.txt)

stations = pd.read_table("data/stations.txt", encoding="unicode_escape")
 ## encoding="unicode_escape" <== to work with symbols like °)


# #%%
# ctd1 = pd.read_csv(
#     "data/ctd-bottles/ctd-bottles-2-1.csv", 
#     na_values=-999
#     )
#  ##-999 is often used instead of NaN... 
# ctd1.plot.scatter("salinity", "depth")

# #%% #!!!HOMEWORK
# # import the variant files... get the same plot

# # This is how it should look like
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/00-ctd-bottles-2-1.csv", 
#     na_values=-999,
#     )
# #%%
# # first 3 rows is general info, so skip in dataframe
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/01-ctd-bottles-2-1.csv", 
#     na_values = -999, 
#     skiprows = 3 #skip first 3 rows 
#     )

# #%%
# # Second row indicates measurement units
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/02-ctd-bottles-2-1.csv", 
#     na_values=-999, 
#     skiprows=[1], #skip second row 
#     encoding="unicode_escape" #to make csv understand ° symbol
#     ) 

# # OR 
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/02-ctd-bottles-2-1.csv", 
#     na_values=-999, 
#     header=[0,1], #assign 2 rows of header to keep the units
#     encoding="unicode_escape"
#     ) 

# #%%
# # first 3 rows with general info, 5th row indicates measurement units
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/03-ctd-bottles-2-1.csv", 
#     na_values=-999, 
#     skiprows=3, #skip first 3 rows
#     header=[0,1], #assign 2 rows of header to keep the units
#     encoding="unicode_escape"
#     )
# # OR
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/03-ctd-bottles-2-1.csv", 
#     na_values=-999, 
#     header=[3,4], #assign 2 rows of header to keep the units
#     # Header automatically skips the row above it
#     encoding="unicode_escape"
#     )

# #%%  
# # .txt file
# ctd1 = pd.read_table(
#     "data/ctd-bottles-variants/04-ctd-bottles-2-1.txt", 
#     na_values=-999, 
#     header=[3,4],
#     encoding="unicode_escape"
#     )

# # OR
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/04-ctd-bottles-2-1.txt", 
#     na_values=-999, 
#     header=[3,4],
#     encoding="unicode_escape",
#     delimiter="\t" #tab delimited txt, 
#     )

# #%%
# # .xlsx file
# ctd1 = pd.read_excel(
#     "data/ctd-bottles-variants/05-ctd-bottles-2-1.xlsx", 
#     na_values=-999, 
#     header=[3,4],
#     )
#   ## already knows the special symbols, so no encoding necesarry

# #%%
# # 2 different NaN values
# ctd1 = pd.read_excel(
#     "data/ctd-bottles-variants/06-ctd-bottles-2-1.xlsx", 
#     na_values=[-999,-777], 
#     header=[3,4]
#     )

# #%%
# # different column names
# ctd1 = pd.read_excel(
#     "data/ctd-bottles-variants/07-ctd-bottles-2-1.xlsx", 
#     na_values=[-999,-777], 
#     header=[3,4]
#     ).rename(columns={
#     'Practical salinity':'salinity',
#     'Depth':'depth'})

# #%%
# # csv with different column names and a footer
# ctd1 = pd.read_csv(
#     "data/ctd-bottles-variants/08-ctd-bottles-2-1.csv", 
#     na_values=[-999,-777], 
#     header=[3,4],
#     skipfooter=3,
#     encoding="unicode_escape",
#     ).rename(columns={
#     'Practical salinity':'salinity',
#     'Depth':'depth'})

# #%%
# ctd1.plot.scatter("salinity", "depth")

#%%
## Parse station information
#row = stations.iloc[1]  #position 0 is the first
  ##.loc to access a row in a dataframe using index
  ##.iloc to access a row using the position in the dataframe

#x = row.Latitude        #results in a string
#x = float(row.Latitude) #results in a numder (float)

#Different lon/lat formats
# 54°00'04"S
# -53.5000
# 50°30.00'S
# https://regex101.com
# (\d+)°(\d+\.\d+)'([NS])

# station = stations.loc[9]

# # regular expression for decimal minutes format
# lat_dmf = re.match("(\d+)°(\d+\.\d+)'([NS])", station.Latitude)
# lat = float(lat_dmf.group(1)) + float(lat_dmf.group(2)) / 60
# if lat_dmf.group(3) == "S":
#     lat *= -1 # *= indicates self * so here: lat * -1
    
# ##!!!HOMEWORK
# # make regular expression for longitude (E/W)
# lon_dmf = re.match("(\d+)°(\d+\.\d+)'([EW])", station.Longitude)
# lon = float(lon_dmf.group(1)) + float(lon_dmf.group(2)) / 60
# if lon_dmf.group(3) == "W":
#     lon *= -1 # *= indicates self * so here: lon * -1


# station = stations.loc[0]
# # make regular expressions for the other format
# lat_dms = re.match("(\d+)°(\d+)'(\d+)\"([NS])", station.Latitude)
# lat = (
#        float(lat_dms.group(1)) 
#        + float(lat_dms.group(2)) / 60
#        + float(lat_dms.group(3)) / 3600
#        )
# if lat_dms.group(4) == "S":
#     lat *= -1 # *= indicates self * so here: lat * -1

# lon_dms = re.match("(\d+)°(\d+)'(\d+)\"([WE])", station.Longitude)
# lon = (
#        float(lon_dms.group(1)) 
#        + float(lon_dms.group(2)) / 60
#        + float(lon_dms.group(3)) / 3600
#        )
# if lon_dms.group(4) == "W":
#     lon *= -1 # *= indicates self * so here: lon * -1
# #%%
# # change all Lon/Lat values in floats instead of strings
# stations["lat"] = np.nan
# stations["lon"] = np.nan
#   ##make new column in the dataframe, with nan as values
# for i, station in stations.iterrows():
#     ## i = index#, station = all info of that row
#     try:
#         lat = float(stations.loc[i, "Latitude"])
#         lon = float(stations.loc[i, "Longitude"])
#         ##try this, if it doesn't work to make a float, continue with except)
#     except:
#         try:
#             dmf = re.match("(\d+)°(\d+\.\d+)'([NS])", (stations.loc[i, "Latitude"]))
#             lat = float(dmf.group(1)) + float(dmf.group(2)) / 60
#             if dmf.group(3) == "S":
#                 lat *= -1
            
#             dmf = re.match("(\d+)°(\d+\.\d+)'([EW])", (stations.loc[i, "Longitude"]))
#             lon = float(dmf.group(1)) + float(dmf.group(2)) / 60
#             if dmf.group(3) == "W":
#                 lon *= -1
#         except:
#             try:
#                 dmf = re.match("(\d+)°(\d+)'(\d+)\"([NS])", (stations.loc[i, "Latitude"]))
#                 minutes = dmf.group(2) + "." + dmf.group(3)
#                 lat = float(dmf.group(1)) + float(minutes) / 60
#                 if dmf.group(4) == "S":
#                     lat *= -1
                
#                 dmf = re.match("(\d+)°(\d+)'(\d+)\"([EW])", (stations.loc[i, "Longitude"]))
#                 minutes = dmf.group(2) + "." + dmf.group(3)
#                 lon = float(dmf.group(1)) + float(minutes) / 60
#                 if dmf.group(4) == "W":
#                     lon *= -1
#             except:
#                 pass

#     stations.loc[i, "lat"] = lat
#     stations.loc[i, "lon"] = lon
    
# # stations.plot.scatter("Longitude", "Latitude")
# #   ##weird plot, because of the symbols in the data

# stations.plot.scatter("lon", "lat")
# #   ##nice plot, but still missing many data points

#!!! With try / pass it passes an error silently... 
#with if, elif else it will raise an error

#%%
# change all Lon/Lat values in floats instead of strings
stations["lat"] = np.nan
stations["lon"] = np.nan
  ##make new column in the dataframe, with nan as values"

# stations.loc[0, "Latitude"] = ""
# stations.loc[1, "Latitude"] = ""
# stations.loc[2, "Longitude"] = ""
# stations.loc[3, "Longitude"] = ""
  
for i, station in stations.iterrows():
    ## i = index#, station = all info of that row

    lat_dmf = re.match("(\d+)°(\d+\.\d+)'([NS])", station.Latitude)
    lat_dmsf = re.match("(\d+)°(\d+)'(\d+)\"([NS])", station.Latitude)
    
             
    if lat_dmf:
        lat = float(lat_dmf.group(1)) + float(lat_dmf.group(2)) / 60
        if lat_dmf.group(3) == "S":
            lat *= -1 # *= indicates self * so here: lat * -1
    
    elif lat_dmsf:
        lat = (
            float(lat_dmsf.group(1)) 
            + float(lat_dmsf.group(2)) / 60
            + float(lat_dmsf.group(3)) / 3600
            )
        if lat_dmsf.group(4) == "S":
            lat *= -1 # *= indicates self * so here: lat * -1   
    
    else:
        lat = float(stations.loc[i, "Latitude"])
    
        
    stations.loc[i, "lat"] = lat
    
    lon_dmf = re.match("(\d+)°(\d+\.\d+)'([EW])", station.Longitude)
    lon_dmsf = re.match("(\d+)°(\d+)'(\d+)\"([EW])", station.Longitude)
    
    if lon_dmf:
        lon = float(lon_dmf.group(1)) + float(lon_dmf.group(2)) / 60
        if lon_dmf.group(3) == "S":
            lon *= -1 # *= indicates self * so here: lon * -1
    
    elif lon_dmsf:
        lon = (
            float(lon_dmsf.group(1)) 
            + float(lon_dmsf.group(2)) / 60
            + float(lon_dmsf.group(3)) / 3600
            )
        if lon_dmsf.group(4) == "S":
            lon *= -1 # *= indicates self * so here: lon * -1   
    
    else:
        lon = float(stations.loc[i, "Longitude"])

    
    stations.loc[i, "lon"] = lon
    
stations.plot.scatter("lon", "lat")
    
    
