
A=(1 3 5 7 9 11 13)
B=(2 4 6 8 10 12)



echo Array_A length: ${#A[@]}
len_A=${#A[@]}
echo Array_B length: ${#B[@]}
len_B=${#B[@]}
i=0
if [ $len_A -gt $len_B ]; then
	len=$len_B
else
	len=$len_A
fi
	while [ $i -le $len ]
	do
		echo loop: $i
		if [ ${#B[$i]} == 0 ]; then
			echo "${A[$i]}" 2>&1 | tee -a temp_1.log
			echo  -n -e " ${A[$i]}" >> temp_2.log
		else
			if [ ${B[$i]} -gt ${A[$i]} ] && [ ${B[$i]} -lt ${A[$i+1]} ] ; then
				#C[$i+1]=${B[$i]}
				#C[$i]=${A[$i]}
				echo  "${A[$i]},${B[$i]}" 2>&1 | tee -a temp_1.log
				echo  -n -e " ${A[$i]}" >> temp_2.log
				echo  -n -e " ${B[$i]}" >> temp_2.log
			fi
		fi
			
	let "i=$i+1"
	done



#echo ${C[@]}	
echo " " >> temp_2.log 
