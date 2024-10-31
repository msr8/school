read -p "Enter a number: " x

fact=1
for ((i=1; i<=x; i++)); do
    fact=$((fact * i))
done

echo "Factorial of $x is $fact"