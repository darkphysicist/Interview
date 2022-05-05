
import sys
import csv
import pandas as pd
import importlib
import argparse
parser = argparse
var = sys.argv[1]
importlib.import_module(var)
var.to_csv('schedule.csv')
var.index
var = read_csv('schedule.csv', index_col=0)
var.describe(include = object)
#this line is for lookups based on schedule.csv
app = sys.argv[2]
importlib.import_module(app)
#this code is for the csv file
def from_dict(cls, column: dict[str, str]) - 
