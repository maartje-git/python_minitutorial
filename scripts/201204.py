import pandas as pd
from matplotlib import pyplot as plt, dates as mdates
from scipy.stats import linregress
import numpy as np
from scipy.optimize import least_squares

filename = "C:/Users/dnalab/Desktop/mini tutorial/201127/co2_mhd_surface-flask_1_ccgg_event.txt"

#making a function out of it
def get_flask_data(filename):
    """Import data from a flask file"""

    with open(filename, "r") as f:  #open file read-only, automatically closed after using
        raw_data = f.read()
    
    #get all lines as seperate strings
    raw_lines = raw_data.splitlines()
    #header_line = raw_lines[67]                # if you know which line and it's always the same line
    # list comprehension
    header_line = [line for line in raw_lines
                   if line.startswith("# data_fields:")]
    header_text = header_line[0]
    header_list = header_text.split(" ")
    #headers = header_list[2:] when it's always the first 2 you want to skip
    #list comprehension
    headers = [h for h in header_list
              if h not in ["#", "data_fields:"]]
    
    #list comprehension long-winded version
    #header_line = []
    #for line in raw_lines:
    #    if line.startswith("# data_fields:"):
    #        header_line.append(line)
    
    #one-line approach of the above
    #with open(filename, "r") as f:
    #    headers = (
    #        [line for line in f.read().splitlines()
    #         if line.startswith("#", "data_fields:")][0]
    #        .split(" ")[2:]
    #        )
    
    flask = pd.read_table(
        filename,
        sep="\s+",              # \s is space, + is regularexpression for 1 or more 
        skiprows=68,
        names=headers,
        )
    
    #get datetime
    dt_cols = {"sample_" + t: t 
               for t in ["year", "month", "day",
                         "hour", "minute"]
        }
    #dict comprehension
    dt_cols["sample_seconds"] = "seconds"       #annoying manual override
    
    #extract date-time columns
    flask["datetime"] = pd.to_datetime(
        flask[dt_cols.keys()].rename(dt_cols, axis=1))    #axis makes it skip the index row
    
    flask["datenum"] = mdates.date2num(flask.datetime)
    
    #QC good data
    flask["xco2_good"] = flask.analysis_flag == "..."
    flask["xco2"] = flask.analysis_value.where(flask.xco2_good)
    
    return flask

#use the function
flask = get_flask_data(filename)

#linear regression
#slope, intercept, r, p, se = linregress(
#    flask[flask.xco2_good].datenum, flask[flask.xco2_good].xco2)

#function for linear regression
def xco2_fit(coeffs, datenum):
    slope, intercept = coeffs
    xco2 = (
        datenum * slope 
        + intercept
        +sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    )
    return xco2

def lsq_xco2_fit(coeffs, datename, xco2):
    return xco2_fit(coeffs, datenum) - xco2

#scipy optimize least squares
#get results as close to 0 as possible 
opt_result = least_squares(lsq_xco2_fit, [0.005, 310], args=(
    flask[flask.xco2_good].datenum, flask[flask.xco2_good].xco2)
)

#visualise
fig, ax = plt.subplots(dpi=300)
flask.plot("datetime", "xco2", ax=ax)
fx = np.array([flask.datenum.min(), flask.datenum.max()])
fy = fx * slope + intercept
fx_datetime = mdates.num2date(fx)
ax.plot(fx,fy)

#visualise
# fig, axs = plt.subplots(ncols=2, dpi=300)
# ax = axs[0]
# flask.plot("datetime", "xco2", ax=ax)
# fx = np.array([flask.datenum.min(), flask.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx,fy)
# ax = axs[1]
# flask.plot("datenum", "xco2", ax=ax)
# fx = np.array([flask.datenum.min(), flask.datenum.max()])
# fy = fx * slope + intercept
# fx_datetime = mdates.num2date(fx)
# ax.plot(fx,fy)
#seaborn
#sns.regplot(x="datenum", y="xco2", data = flask[::40], ax=ax, ci=99.9)
