echo 'Enter Directory name'
read d

echo '***MENU***'
echo 'Type 1 for short desc'
echo 'Type 2 for long desc'
echo 'Type 3 for hidden file display'

read ch

case "${ch}" in 
    1) ls $d
    ;;
    2) ls -l $d
    ;;
    3) ls -la $d
    ;;
    *)echo "Invalid Choice"
    ;;
esac





