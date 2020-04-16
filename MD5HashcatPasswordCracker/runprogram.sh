#!/bin/bash
python createhash.py
echo Did you input a birthday or a studentID? Enter b or s. If neither, put n.
read typeofinput
if [ $typeofinput == 'b' ]
then
   birthday=`hashcat -a 0 -m 0 hash.hash birthdays.dict --force`
   echo "$birthday"
   echo "$birthday" >> hashcatresults.txt
   echo 'printed results to hashcatresults.txt'
elif [ $typeofinput == 's' ]
then
    studentid=`hashcat -a 0 -m 0 hash.hash Lancessuccess.dict --force`
    echo "$studentid"
    echo "$studentid" >> hashcatresults.txt
    echo 'printed results to hashcatresults.txt'
elif [ $typeofinput == 'n' ]
then
    passwordtestinglength=`hashcat -a 3 -m 0 -i --increment-min=1 --increment-max=15 hash.hash ?d?d?d?d?d?d?d?d?d?d?d?d?d?d --force`  
    echo "$passwordtestinglength"
    echo "$passwordtestinglength" >> hashcatresults.txt
    echo 'printed results to hashcatresults.txt'
else
    echo 'nothing recognized, try again'
fi
