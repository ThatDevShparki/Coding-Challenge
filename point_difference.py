#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Ryan Sheppard
# Date: 5/19/20
# -------------------------
# Description:
# This code prints the smallest point differential between points for and points against
# amongst all soccer teams in the file. 

# import pandas, re
import pandas as pd
import re

# define the location of the data
loc = 'soccer.dat'

# load the data into a list containing each value from that line
file = []
with open(loc,'r') as f:
    file += [line.split() for line in f]  
    
# remove invlaid symbols from the data and create a list of lists for each row
trim_file = [[val for val in f[1:] if re.search(r'[^\w_]',val) == None] for f in file if len(f) > 7]
    
# load into a data frame and set the index to the team
df = pd.DataFrame(trim_file[1:],columns=['Team'] + trim_file[0]).set_index('Team')

# cast the column values to integers
for col in df.columns:
    df[col] = df[col].astype(int)

# add difference between the F and A Columns as a new column in the dataframe 
df['Diff'] = df.apply(lambda row : row['F'] - row['A'], axis = 1)

# find the minimum value for the new column and print the corresponding
# team, differential, points for, and points against
print('The team with the lowest point differential is', \
      df['Diff'].idxmin(), 'with a point differential of',df['Diff'].min())
print('Points For: ', str(df.loc[df['Diff'].idxmin()].F))
print('Points Against: ', str(df.loc[df['Diff'].idxmin()].A))