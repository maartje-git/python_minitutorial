# =============================================================================
# Python mini tutorial
# 210525
# Strings
# =============================================================================

x = 'Abcdefg'
y = "12345"

quote = 'The man said "hello"'
quote = "The man said \"hello\""

# multi-line string
z = 'one\ntwo'
z2 = '''one
two
three'''

# string methods
# https://www.w3schools.com/python/python_ref_string.asp
x_length = len (x)

# look if one string appears in another
x_has_abc = 'abc' in x
y_has_abc = 'abc' in y
x_abc_at_start = x.startswith('abc')
x_abc_at_end = x.endswith('abc')
x_find_de = x.find('de') # abcdefg / 0123456, so de starts at 3
y_find_de = y.find('de') # no de, so -1

# convert case
x_upper = x.upper()
x_lower = x.lower()
# combine to make search case insensitive
x_abc_at_start_case = x.lower().startswith('abc')

# splitting
sample = 'DY33 3 11'
sample_split = sample.split() # default is white space
sample2 = 'DY33-3-11'
# sample2_split = sample2.split('-')
station, cruise, niskin = sample2.split('-')

# splitting lines
z_lines = z.split('\n')
z_lines_auto = z.splitlines()

# joining
xy = x + y
# same
xy_joined = '-'.join((x, y, 'more', 'evenmore')) 

# format
phrase = 'My name is {}. {} {}.'.format(
    'Bond', 'James', 'Bond'
)
# default is number you provide the arguments
phrase = 'My name is {0}. {1} {0}.'.format(
    'Bond', 'James'
)
# positional arguments 
phrase = 'My name is {surname}. {firstname} {surname}.'.format(
    surname='Bond', firstname='James'
)
# keyword arguments
print (phrase)

#%%
# format with numbers
import numpy as np
print ('The value of pi is '+ str(np.pi))
# better using format
print('The value of pi is {}'.format(np.pi))
# https://www.w3schools.com/python/ref_string_format.asp
# format how many decimals you want
print('The value of pi is {:.3f}'.format(np.pi)) #float point with 3 decimals
# change alignment
print('The value of pi is {:10.3f}'.format(np.pi)) #float is 10 characters
print('The value of pi is {:<17.3f}'.format(np.pi)) #left align
print('The value of pi is {:^17.3f}'.format(np.pi)) #centre align
print('The value of pi is {:>17.3f}'.format(np.pi)) #right align
# Pad with zeros
print('The value of pi is {:010.3f}'.format(np.pi)) #fill-up with zeros to 0s
print('The value of pi is {:010.0f}'.format(np.pi)) #no decimals, fill with 0s
print('The value of pi is {:^010.0f}'.format(np.pi)) #not OK ;)
print('The value of pi is {:^010.1f}'.format(np.pi)) #OK ;)
print('The value of pi is {:.3f}'.format(-np.pi)) #negative pi
print('The value of pi is {:+.3f}'.format(np.pi)) #negative pi

#%%
# add strings to a figure
from matplotlib import pyplot as plt

#make empty plot
fig, ax = plt.subplots(dpi=300)

#add title
# for equations: use latec formatting use $$ (makes it italic)
ax.set_title('$R^2$ = {r2:.3f}, $n$ = {n}'.format(r2=0.56484536,
                                             n=50))

# add labels (superscript ^, subscript _)
ax.set_xlabel("Molality of CO$_2$ / µmol kg$^{-1}$")

# format and latec formatting at once (both use {})
# put the .format right where it's needed, for instance:
# ax.set_xlabel("Molality / mol {} kg".format('-') + "$^{-1}$")

#%%
# string methods and pandas arrays
import pandas as pd

coccos = pd.read_csv('python_minitutorial/raw_data/Poulton_v2.csv')

# look for references in specific year
# refs_2011 = coccos.Reference.endswith('2011') 
# tries to access all
refs_2011 = coccos.Reference[1].endswith('2011') 
#True or false for specific row
refs_2011 = coccos.Reference.str.endswith('2011') # to access entire dataframe
# add into dataframe
coccos['published_2011'] = coccos.Reference.str.endswith('2011')

























      