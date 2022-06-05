#!bin/bash

echo 'Enter new Dirctory name'
read dir

mkdir -p $dir

echo 'Enter no of files'
read n

for((i=0;i<$n;i++)); do
    echo 'Enter file name'
    read f
    cp $f $dir
done


