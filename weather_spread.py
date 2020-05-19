#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Ryan Sheppard
# Date: 5/19/20
# -------------------------
# Description:
# This code prints the smallest spread between the maximum and minimum temperatures
# for a given day in the data. 

# import pandas, re
import pandas as pd
import re

# define the location of the data
loc = 'w_data (5).dat'

# load the data into a list containing each value from that line
file = []
with open(loc,'r') as f:
    file += [line.split() for line in f]
    
# remove invalid symbols to create a list of lists for the first three values in each row
trim_file = [[re.sub(r'[^\w.]','',val) for val in f[:3]] for f in file if len(f) > 10]

# convert the list to a dataframe and set the index to days
df = pd.DataFrame(trim_file[1:],columns=trim_file[0]).set_index('Dy')

# cast the column values to integers
for col in df.columns:
    df[col] = df[col].astype(int)
    
# add the spread between the max and min temperatures as a new column  
df['Spread'] = df.apply(lambda row : row['MxT'] - row['MnT'], axis = 1)
      
# find the minimum value for the new column and print the corresponding
# day, temperature spread, max temp, min temp
print('The day with the smallest temperature spread is Day', \
      df['Spread'].idxmin(), 'with a spread of',str(df['Spread'].min()))
print('Maximum Temperature:', str(df.loc[df['Spread'].idxmin()].MxT))
print('Minimum Temperature:', str(df.loc[df['Spread'].idxmin()].MnT))
