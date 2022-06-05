!#bin/bash

echo 'Enter the file to read : '
read f

echo 'No. of lines'
wc -l < $f

echo 'No. of words'
wc -w < $f

echo 'No. of characters'
wc -c < $f

