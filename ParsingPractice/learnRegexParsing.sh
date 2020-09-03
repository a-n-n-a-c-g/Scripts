thingtolookfor=$1
string=`cat fileToParse.conf`
theline=$(echo $string | awk -vRS="};" -vFS="{" '{print $2}' | grep $thingtolookfor | awk -vRS="]" -vFS="[" '{print $2}' | awk -vRS="/" -vFS="/" '{print $1}')
count=$(echo $theline | wc -w)
array=( $theline )
column_two=()
column_one=()
column_three=()
col3_3_array=()
newCounter=0
for i in $(seq 1 $count);
do 
   j=$i-1
    #echo $i:${array[$j]} 
        if (( $i%3==2 )); then
        column_two+=(${array[$j]})
        col3_3_str=$(echo ${array[$j]} | awk -vRS="." -vFS="." '{print $1}')
        col3_3_format=$(echo $col3_3_str | cut -d " " -f3)
        col3_3_array_entry=$col3_3_format" "
        #echo "col3_3_array_entry="$col3_3_array_entry >> formatted-out.$col3_3_array_entry
        col3_3_array+=$col3_3_array_entry
        newCounter=$(grep -o $col3_3_array_entry <<< ${col3_3_array[*]} | wc -l)
        if [ $newCounter == 1 ]; then
            echo "COL_2="${array[$j]} >> formatted-out.$col3_3_array_entry
        else
            echo "COL_2"$newCounter"="${array[$j]} >> formatted-out.$col3_3_array_entry
        fi
    elif (( $i%3==0 )); then
        column_three+=(${array[$j]})
        if [ $newCounter == 1 ]; then
            echo "COL_3="${array[$j]} >> formatted-out.$col3_3_array_entry
            echo "col3_3_array_entry="$col3_3_array_entry >> formatted-out.$col3_3_array_entry
        else
            echo "COL_3"$newCounter"="${array[$j]} >> formatted-out.$col3_3_array_entry
        fi
    else
        column_one+=(${array[$j]})
    fi
done
#echo column_one:${column_one[@]}
#echo column_three:${column_three[@]}
#echo column_two:${column_two[@]}
#echo col3_3_array:${col3_3_array[@]}
if [ ${#column_one[@]} == ${#column_three[@]} ] && [ ${#column_one[@]} == ${#column_two[@]} ]; then
    echo "it all works";
else echo "something failed"
fi
