
A=(11 3 15 7 29 33 13)


len=${#A[@]}
#echo $len
i=0
while [ $i -lt $len ]
do
	k=0
	for ((j=0;j<$len;j++))
	do
		#echo A:$i , ${A[$i]}, J:$j
		if [ ${A[$i]} -gt ${A[$j]} ]; then
			let "k=$k+1"
			#echo B:$k
		fi
		#let "j=$j+1"
	done
	#echo "B[$k]=${A[$i]}"
	B[$k]=${A[$i]} 

	#echo ${B[@]}
let "i=$i+1"
done
echo ${B[@]}
