// This will be the connector to the files
# based on what is put into the command line I want to create 
a path to the schedule file, the chosen app file, and the 
#output example file where the result will go
#the code will create a path to the appfile chosen and look at the names
#each name will be compared to the same name in the schedule text file
#Once the correct one is found it will then print out everything within that row

import argparse
parser = argparse

#this code is for the csv file
def from_dict(cls, column: dict[str, str]) - 
> "Schedule":
    if column["Disabled"] = true 
    return None
    else
    return row
