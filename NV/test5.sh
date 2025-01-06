
A=(1 3 5 7 9)
B=(2 4 6 8 10 11)
i=0
j=0
k=0
while [ $i -lt ${#B[@]} ];
do
echo ${A[i]}
echo ${B[i]}

if [ ${A[i]} -gt ${B[i]} ]; then
	C[$i]=${B[i]} 
	C[$(echo $(($i+1)))]=${A[i]} 
else
	C[$i]=${A[i]} 
	C[$(echo $(($i+1)))]=${B[i]} 
fi
	



((i++))
done

