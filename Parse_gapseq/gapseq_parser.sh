#/usr/bin/bash

#Make sure the script "handle.py" is in the same folder of this script or give it's path.
mkdir processed_niche

#Select from gapseq pipeline only the columns with "true" predictions, the pathways names and completeness.

for k in *Pathways.tbl; do ps -ef |  awk -F '\t' 'NR==1{print $2"\t"$4} /true/{print $2"\t"$4}'  $k > ./processed_niche/${k%-all-Pathways.tbl}.tbl; done

cd processed_niche

#Rename all files to leave only the species names and the extension

for i in *tbl; do mv "$i" "$(echo $i | awk -F"_" '{print $3"_"$4}')"; done

for f in *tbl; do sed -i '1s/Completeness/'"$f"'/' $f; done

python $Path/to/handle.py

sed -i -e 's/.tbl//g' *.tsv

echo "DONE"
