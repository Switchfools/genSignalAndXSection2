#!/bin/bash

# check input arguments
if [ "$#" -ne 4 ]; then
    echo "Need 4 parameters to run: n1, n2, n3, and j0"
    exit 2
fi

n1=$1
n2=$2
n3=$3
j0=$4

echo Using n1 = $n1, n2 = $n2 , n3 = $n3, j0= $j0

currentFolder=/home/nvergara/genSignalAndXSection2/xSection/
outputFolder=/home/nvergara/genSignalAndXSection2/results/xSection/n1_${n1}_n2_${n2}_n3_${n3}_j0_${j0}/

# create mg5 file
rm ${currentFolder}currentRun/*

cp ${currentFolder}templates/standardMgFile.mg5 ${currentFolder}currentRun/mgFile.mg5
#cp ${currentFolder}templates/run_card.dat ${currentFolder}currentRun/run_card.dat
#cp ${currentFolder}templates/standardParamCard.dat ${currentFolder}currentRun/param_card.dat

# create ouput folder
mkdir -p $outputFolder

sed -i "s|outputFolder|${outputFolder}|g" ${currentFolder}currentRun/mgFile.mg5

echo "launch ${outputFolder}" >> ${currentFolder}currentRun/mgFile.mg5
echo "set mN1 ${n1}" >> ${currentFolder}currentRun/mgFile.mg5
echo "set mN2 ${n2}" >> ${currentFolder}currentRun/mgFile.mg5
echo "set mN3 ${n3}" >> ${currentFolder}currentRun/mgFile.mg5
echo "set MJ ${J0}" >> ${currentFolder}currentRun/mgFile.mg5
echo "set nevents 500" >> ${currentFolder}currentRun/mgFile.mg5
echo "set deltaeta 2.4" >> ${currentFolder}currentRun/mgFile.mg5

#log the output for post processing
echo "running mg5_aMC ${currentFolder}currentRun/mgFile.mg5"
script -c "mg5_aMC ${currentFolder}currentRun/mgFile.mg5" -q ${currentFolder}logXSection.txt

# remove files from output folder. They are too heavy
rm -rf ${outputFolder}/*

cp ${currentFolder}logXSection.txt "${outputFolder}xsectionLog.txt"

# get cross section values
xsection=$(cat ${currentFolder}logXSection.txt | grep "Cross-section" | awk '{print $3}')
xsectionerr=$(cat ${currentFolder}logXSection.txt | grep "Cross-section" | awk '{print $5}')
nevents=$(cat ${currentFolder}logXSection.txt | grep "Nb of events" | awk '{print $5}')

echo "xsection = $xsection, xsectionerr = $xsectionerr and nevents = $nevents"
echo "saving results to ${outputFolder}xsection.dat"

#write them to file
echo "n1,n2,n3,j0,xsection,xsectionerr,nevents" > "${outputFolder}xsection.dat"
echo "${n1},${n2},${n3},${j0},${xsection},${xsectionerr},${nevents}" >> "${outputFolder}xsection.dat"

# remove temp logXsection file
rm ${currentFolder}logXSection.txt
