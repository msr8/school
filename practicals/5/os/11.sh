read -p "Enter a number: " num
echo "Table of $num:"
for i in {1..10}; do
    echo "$num * $i = $((num * i))"
done
