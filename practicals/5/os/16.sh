read -p "Enter three numbers: " a b c

if [[ $a -ge $b && $a -ge $c ]]; then
    grt=$a
elif [[ $b -ge $a && $b -ge $c ]]; then
    grt=$b
else
    grt=$c
fi

echo "$grt is the greatest number"
