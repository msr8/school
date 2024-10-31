read -p "Enter a number: " x

if (( x <= 1 )); then
    echo "$x is not a prime number"
    exit
fi

is_prime=1
for ((i=2; i<=x/2; i++)); do
    if (( x % i == 0 )); then
        is_prime=0
        break
    fi
done

echo -n "$x is "
if (( is_prime == 1 )); then
    echo "a prime number"
else
    echo "not a prime number"
fi