# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import sys
import fileinput
from Utility.parameters import DUMP_DIR
# get the csv file
filename = DUMP_DIR + '\\' + 'WCHEALTH_missoula_2018_Apr_18_03.32.44.csv'
# check for duplicate rows and remove

seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput(filename, inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    sys.stdout.write (line, ) # standard output is now redirected to the file

# output csv
