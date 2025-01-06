A=(2 16 19 28 32 96)
B=(1 8 14 17 30)


len1=${#A[@]}
len2=${#B[@]}
k=0

if [ $len1 -gt $len2 ]; then

	len=len1
else
	len=len2
fi

for ((i=0;i<$len;i++))
do
	echo i:$i
	
	if [ "${A[$i]}" == "" ]; then
		 A[$i]=0
	fi
	if [ "${B[$i]}" == "" ]; then
		 B[$i]=0
	fi
	echo "${A[$i]} , ${B[$i]},"
	if [ ${A[$i]} -gt  ${B[$i]} ]; then
		
		C[$k]=${B[$i]}
		C[$k+1]=${A[$i]}
		
	else
		
		echo ${A[$i]}
		if [ ${A[$i]} == 0  ]; then
			#C[$k]=${A[$i]}
			C[$k+1]=${B[$i]}
			
		else
			C[$k]=${A[$i]}
			C[$k+1]=${B[$i]}
				

		fi
		if [ ${B[$i]} == 0  ]; then
			C[$k]=${A[$i]}
			#C[$k+1]=${B[$i]}
			
		else
			C[$k]=${A[$i]}
			C[$k+1]=${B[$i]}
				

		fi
		#break	
			
	fi
	echo k:$k
	let "k=$k+2"
	echo ${C[@]}
	

done		





