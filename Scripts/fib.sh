echo "Enter nos of fibonacci (length)"
read n

let a=0
let b=1

echo 'Fibonacci series : '

for((i=0;i<$n;i++)); do
    echo "$a"
    c=$((a+b))
    a=$b
    b=$c

done