
A=(1 3 5 7 9 11 13 15 17 19 21)
B=(2 4 6 8 10 12 14 16 18 20 22 24 26)


rm -f temp_1.log
rm -f temp_2.log
echo Array_A length: ${#A[@]}
len_A=${#A[@]}
echo Array_B length: ${#B[@]}
len_B=${#B[@]}
i=0
if [ $len_A -gt $len_B ]; then
	
	len=$len_A

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
else
	len=$len_B
	
	while [ $i -le $len ]
	do
		echo loop: $i
		echo  "${A[$i]},${B[$i]}"
		if [ ${#A[$i]} == 0  ]; then
			echo "${B[$i]}" 2>&1 | tee -a temp_1.log
			echo  -n -e " ${B[$i]}" >> temp_2.log
		
		elif [ ${A[$i]} -lt ${B[$i]} ] && [ ${#A[$i+1]} == 0 ] ; then
				#C[$i+1]=${B[$i]}
				#C[$i]=${A[$i]}
				echo  "${A[$i]},${B[$i]}" 2>&1 | tee -a temp_1.log
				echo  -n -e " ${A[$i]}" >> temp_2.log
				echo  -n -e " ${B[$i]}" >> temp_2.log
		

		elif [ ${A[$i]} -lt ${B[$i]} ] && [ ${A[$i+1]} -gt ${B[$i]} ] ; then
				#C[$i+1]=${B[$i]}
				#C[$i]=${A[$i]}
				echo  "${A[$i]},${B[$i]}" 2>&1 | tee -a temp_1.log
				echo  -n -e " ${A[$i]}" >> temp_2.log
				echo  -n -e " ${B[$i]}" >> temp_2.log

		else
			echo "abnormal array"			
				exit
		fi
			
	let "i=$i+1"
	done
	#echo ${C[@]}	
	echo " " >> temp_2.log 

fi


echo
	cat temp_2.log
echo
