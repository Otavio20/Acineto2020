#usr/bin/python
import pandas as pd
import re
import numpy as np
from io import StringIO
import glob
import os
from functools import reduce

###Count number of genes after blast filtering (higher e-value and identity thresholds)
blast=glob.glob(os.path.join('*.csv'))
lista=[]
for f in blast:
        fhands=pd.read_csv(f ,header=0, error_bad_lines=False, sep='\t')
        lista.append(fhands)

df=pd.concat(
    (iDF.set_index('Categories') for iDF in lista),
    axis=1, join='inner'
).reset_index()

df.to_csv("COGs.csv", index = False)
print("All done!")
