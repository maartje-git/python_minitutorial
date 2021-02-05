import pandas as pd, numpy as np
#scientific python module scipy.org
from scipy import stats

data = pd.read_csv(
    "../raw_data/MgCa_data_field.csv")

#edit things in code, so you don't have to change everything seperately
data.rename(columns={"Del-CO32-": "delCO3", "T": "temperature"}, inplace=True)

#do linear regression
#.values na luisteren
l = ~np.isnan(data.temperature) & ~np.isnan(data.delCO3)
slope, intercept, r, p, se = stats.linregress(data[l].temperature.values,
                                            data[l].delCO3.values)

