#!/bin/bash

echo -e "Enter First No : \c"
read a

echo -e "Enter Second No : \c"
read b

echo -e "Enter Last No : \c"
read c

if [ $a -gt $b ] && [ $a -gt $b ] 
then
    echo " $a is biggest"
elif [ $b -gt $a ] && [ $b -gt $c ] 
then
    echo " $b is biggest"
else 
    echo " $c is biggest"
fi

