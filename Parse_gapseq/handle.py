#/usr/bin/python

import pandas as pd
import glob
import os
#Read files
file=glob.glob(os.path.join('*.tbl'))
lista=[]
for f in file:
        fhands=pd.read_csv(f ,header=0, error_bad_lines=False, sep='\t')
        lista.append(fhands)
#Join files based on common shared rows
df=pd.concat((iDF.set_index('Name') for iDF in lista), axis=1, join='inner', sort=True).reset_index()

df.to_csv("intersection.tsv", index = False, sep='\t')
print("Generated intersection file!")
#Join files considering all rows
df1=pd.concat((iDF.set_index('Name') for iDF in lista), axis=1, join='outer', sort=True).reset_index()
df1=df1.fillna(0)
df1=df1.loc[(df1.sum(axis=1) != 0), (df1.sum(axis=0) != 0)]
df1=df1.rename(columns={'index':'Name'})
df1.to_csv("all_data.tsv", index = False, sep='\t')
print("Generated all_data file!")

#Make a dataframe with all metabolic pathways

df2=pd.read_csv('all_data.tsv' ,header=0, error_bad_lines=False, sep='\t')

#Make a dataframe with all metabolic pathways shared by 100% of the species

df3=pd.read_csv('intersection.tsv',header=0, error_bad_lines=False, sep='\t')

#Make a dataframe with the metabolic pathways that are not present in all species 

data = df3.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']

data.to_csv("Differences.tsv", index=False, sep='\t')

print("Generated Difference file!")
