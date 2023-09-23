import os
import pandas as pd
import csv
f = open(os.getcwd() + '\\user.csv','r')
rdr = csv.reader(f)
 
for line in rdr:
    print(line)
 
f.close()