read -p "Enter a character: " char

echo -n "$char is "

if [[ $char =~ [A-Z] ]]; then
    echo "an uppercase letter"
elif [[ $char =~ [a-z] ]]; then
    echo "a lowercase letter"
elif [[ $char =~ [0-9] ]]; then
    echo "a digit"
fi