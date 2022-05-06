
import sys
import csv
import pandas as pd
import importlib
import argparse
parser = argparse
var = sys.argv[1]
importlib.import_module(var)
var.to_csv('schedule.csv')
colspecs = [(2, 20), (22, 62), (64, 72), (77, 85), (88, 93), (99, 107)}
var.pd.read_fwf('schedule.txt', skiprows = 2, colspecs = colspecs, names = ['Application', 'Options', 'Start', 'Disabled', 'Schedule'])
var.describe(include = object)
#this line is for lookups based on schedule.csv
app = sys.argv[2]
importlib.import_module(app)
colspecs = [(2, 20), (22, 62), (64, 72), (77, 85), (88, 93), (99, 107)}
filepath = app
with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line, i < size, i++:
            if(fp[i] = var[i])
            display(var.ilo[i](
            else if(fp[i] != var[i])
            i++
            else
            return 0
