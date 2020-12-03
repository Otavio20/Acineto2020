#usr/bin/bash

#The eggNOG mapper results in one file with the extesion ".annotations" by each genome protein dataset blasted against the eggNOG database. The script "parse_COGS.sh" must be placed in the same dir containing the script "extract_COGs_v2.sh" ( original name: extract_COG_local_v2.0.sh created by https://github.com/raymondkiu/eggnog-mapper_COGextraction) and "merge.py". Initially, the script rename the files (that obey the structure: GCF_"numberXXX"_Acinetobacter_species) and then through several loops and the external scripts it builds a count table containing all COG categories summarized by each strain or species under study.

#Rename files to leave only the species name and the extension

for i in *annotations; do mv "$i" "$(echo $i | awk -F"_" '{print $3"_"$4}').annotations"; done

#Extract COGs

for f in *annotations; do  bash /root/scripts_utilities_Otavio/COG/extract_COGs_V2.sh $f; done

###Prepare files to input in the Python script

echo "Naming files"

for file in *COG-final.csv; do  awk 'NR==1 { print "Categories",  FILENAME }; 1' "$file" > temp && mv temp "$file"; done

for f in *COG-final.csv; do sed -i 's|,|\t|g' $f; done

for fact in *COG-final.csv; do awk '{$1=$1}1' OFS="\t" "$fact" > temp && mv temp "$fact" ; done

mkdir COGS_parsed_output

mv *COG-final.csv COGS_parsed_output/

cd COGS_parsed_output/

echo "Making count table!"

python /root/scripts_utilities_Otavio/COG/merge.py
