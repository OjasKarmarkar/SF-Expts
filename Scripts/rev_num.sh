#!/bin/bash
rev=0

echo -e 'Enter no of digits : \c'
read d

echo -e 'Enter number : \c'
read num

while [ $d -gt 0 ]
do
    x=$((num % 10))
    rev=$((rev*10 + x))
    num=$((num/10))
    d=$(( d-1 ))
done

echo "Reversed Number : $rev"

