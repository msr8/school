let x = prompt("Enter a number:");
let i=x;
let product=1;

while (i!=1) {
    product *= i;
    i = i-1;
}

alert(`The factorial of ${x} is ${product}`);

