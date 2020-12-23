#! /bin/bash
# TO USE THIS, CREATE goal.txt THAT HAS THE HASH YOU WANT

goal=`cat goal.txt`
echo "input"
read input
#echo -n $input | sha256sum
#hashed=($(sha256sum "$input"))
#goal=`echo -n "test" | sha256sum > test.txt`
echo -n "$input" | sha256sum > hash.txt
hashvalue=`cat hash.txt`

echo "your input given "$hashvalue
echo "the goal hash is "$goal

if cmp -s "hash.txt" "test.txt"; then
	echo "correct!"
else
	echo "wrong"
fi
