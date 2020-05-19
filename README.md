# Coding-Challenge

### Files:
weather_spread.py, point_difference.py, w_data (5).dat, soccer.dat

### Description

The following two programs find the minimum difference between two columns in different sets of data. 

The weather_spread.py program evaluates daily data from the w_data (5).dat file. The data is in the form of text file with several invalid values. The program cleans the data and formats a pandas data frame with the Max Temperature, Minimum Temperature, and the Difference between the two values for each day. The minimum value from the final column is printed along with the corresponding values for that row.

The point_difference.py program evaluates soccer team data from the soccer.dat file. The data also is in the form of text file with several invalid values and rows. The program cleans the data and formats a pandas data frame with all of the data and adds a column to specify the spread between the points scored by the team and points scored against the team. The minimum value for this final column is printed along with the team Name, the Points Scored For, and the Points Scored Against.

After completing the first program, I realized the importance of understanding the data and developing a more robust approach when data cleaning, which becomes more relevant as data scales. In the first data set, random values across the text contain * symbol. It was important to check each value in order to remove unwanted symbols, hence the use of the re package. If you would have done the second program first, you might have assumed that both data sets could have utilized hard coded indices to avoid unwanted symbols in the data. In general, this is a bad practice.

### Prerequisites

In order to run both of the Python programs, you must have both pandas and re installed and the corresponding data files. When running the programs, make sure the data files are in the same location. Otherwise, you will need to edit the file location in the python code. 


## Results

weather_spread.py Output:

The day with the smallest temperature spread is Day 14 with a spread of 2
Maximum Temperature: 61
Minimum Temperature: 59

point_difference.py Output:

The team with the lowest point differential is Leicester with a point differential of -34
Points For:  30
Points Against:  64

## Authors

Ryan Sheppard

## Acknowledgments

Thank you for the Coding Challenge! I truly enjoyed it and I look forward to the next steps!
