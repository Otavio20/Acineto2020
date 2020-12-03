#usr/bin/python
import pandas as pd

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
