=csv Analyzer=

A program which does a quick analysis of a .csv file. The program can do the following
operations on a .csv file:
- Display the first 5 items for the first 5 columns in the file.
  - If there are more than 5 items and columns, they are abbreviated.
- Calculate and display the median for each column.
- Calculate and display the mean for each column.

For variables that are categorical, the mean and median is not computed.

<Usage>
use: [option] [.csv file path] (Ex. "ruby csvanalyzer.rb -d data.csv")

options:
[-d]: Displays data
[-m]: Display median
[-a]: Display average
