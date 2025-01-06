
#B=(1 8 2 9 14 11 17 15 18 16 30 19 28 101 99 55 33 29)
#B=(1 2 8 16 14 19 17 28 30 45 0 69)
#unset B[10]
#echo ${B[@]} > temp_1.log
a=0
unset B
while read line
do

B[$a]=$( echo $line )
echo ${B[$a]}
((a++))


done < temp_1.log

echo ${B[@]}

echo GG

for ((i=0; i<${#B[@]}; i++))
do
	for ((j=0; j<${#B[@]}; j++))
	do	
	first=${B[$j]}
	second=${B[$j+1]}
	#echo $first
	#echo $second
	if [ "$second" != "" ]; then
		if [ $first -gt $second ]; then
			temp=$first
			B[$j]=$second
			B[$j+1]=$temp
		fi
	fi
done
done
echo ${B[@]}
		



