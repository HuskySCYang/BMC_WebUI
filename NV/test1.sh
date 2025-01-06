A=(2 16 19 28)
B=(1 8 14 17 30)


merge(){
C=(${A[@]} ${B[@]})
#echo ${C[@]}

len=${#C[@]}
#echo $len
for ((i=1;i<$len;i++))
do
	for ((j=0;j<$len-1;j++))
	do
	first=${C[$j]}
	second=${C[$j+1]}
		if [ $first -gt $second ]; then
			temp=$first
			C[$j]=$second
			C[$[j]+1]=$temp
		fi
	done

done
echo ${C[@]}
}


len1=${#A[@]}
len2=${#B[@]}
k=0

for ((i=0;i<$len1;i++))
do
	
	for ((j=0;j<$len2;j++))
	do
	echo "${A[$i]} , ${B[$j]}, ${B[$j+1]}"
	if [ ${A[$i]} -gt  ${B[$j]} ] && [ ${A[$i]} -lt  ${B[$j+1]} ] ; then
		
		C[$k]=${B[$j]}
		C[$k+1]=${A[$i]}
		C[$k+2]=${B[$j+1]}

		
		
	fi
	echo k:$k
	let "k=$k+1"
	echo ${C[@]}
	done

done		
D=${C[@]}
echo $D
f=0
len_3=${#C[@]}
#echo $len3
for ((h=0; h<$len_3 ;h++))
do
	echo "H:$h, >> ${C[$h]}"
	#for ((s=0; s<$len3 ;s++))
	#do	
	#echo 3: ${C[3]},
	#echo h:$h, ${C[$h]}
	#echo ${C[$h]},${C[$s]}
	#echo s:$s, ${C[$s]}
	#if [ ${C[$h]} == ${C[$s]} ]; then
	#	let "f=$f+1"
	#	if [ $f -gt 1 ]; then
	#		echo gg
	#	fi
	#fi
	#done
done
#echo ${C[@]}


