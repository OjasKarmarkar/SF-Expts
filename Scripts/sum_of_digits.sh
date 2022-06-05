#!/bin/bash

sum=0

echo -e 'Enter no of digits : \c'
read d

echo -e 'Enter number : \c'
read num

while [ $d -gt 0 ]
do
    digit=$((num%10))
    sum=$((sum+digit))
    num=$((num/10))
    d=$((d-1))
done

echo $sum