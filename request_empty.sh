#!/bin/bash

INPUT="error.log"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read zip
do
    cat zip_coordinates.txt | grep $zip >> temp.txt
done < $INPUT

INPUT=temp.txt
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read zip lat lng
do
    echo "Current Zip $zip"
    wget -O "raw/$zip.json" "https://www.dekalbasgrowdeltapine.com/en-us/local-yield-results/_jcr_content/root/responsivegrid/harvest_results.harvest.json?brand=dekalbasgrowdeltapine&crop=corn&crop=cotton&crop=silage&crop=soybeans&year=2017&year=2018&year=2019&year=2020&lat=$lat&lng=$lng&radius=25"
done < $INPUT
IFS=$OLDIFS

rm temp.txt
