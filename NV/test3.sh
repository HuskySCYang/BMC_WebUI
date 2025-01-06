A=(2 16 19 28 45 69)
B=(1 8 14 17 30)
unset C
#C=${B[@]]

len1=${#A[@]}
len2=${#B[@]}
k=0


if [ $len1 -gt $len2 ]; then
	len=$(echo $[ $len1 - $len2])
	for ((a=0;a<$len;a++))
	do
	echo "B[$len2+$a]=0"
	
	B[$len2+$a]=0
	done
else
	len=$(echo $[ $len2 - $len1])
	for ((a=0;a<$len;a++))
	do
	echo "A[$len1+$a]=0"
	
	A[$len1+$a]=0
	done
fi
unset D
echo len: $len
D=${A[@]}
echo ${B[@]}
len3=${#A[@]}

for ((i=0;i<$len3;i++))
do
	
	echo i:$i
	echo "${A[$i]} , ${B[$i]}"
	if [ ${A[$i]} -gt  ${B[$i]} ]; then
		
		C[$k]=${B[$i]}
		C[$k+1]=${A[$i]}
		
	else
		C[$k+1]=${B[$i]}
		C[$k]=${A[$i]}
		
	fi

	echo k:$k
	let "k=$k+2"
	echo ${C[@]}
	
	

done		

for ((b=0; b< ${#C[@]}; b++))
do
	if [ "${C[$b]}" == "0" ]; then
		unset C[$b]
	fi
done

echo ${C[@]} > temp_1.log
sed -i 's/ /\n/g' temp_1.log 


a=0
while read line
do

D[$a]=$(echo $line)
#echo ${D[$a]}
((a++))
done < temp_1.log

for ((i=0; i<${#D[@]}; i++))
do
	for ((j=0; j<${#D[@]}; j++))
	do	
	first=${D[$j]}
	second=${D[$j+1]}
	#echo $first
	#echo $second
	if [ "$second" != "" ]; then
		if [ $first -gt $second ]; then
			temp=$first
			D[$j]=$second
			D[$j+1]=$temp
		fi
	fi
done
done
echo ${D[@]}
		
