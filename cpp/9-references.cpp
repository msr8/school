#include <iostream>
using namespace std;



void swap(int& x, int& y) {
    int temp = x;
    x = y;
    y = temp;
}


int main() {
    int  x=8;
    int& x_ref=x;
    cout << "x = " << x << " | x_ref = " << x_ref <<endl<<endl;

    cout << "Changing x to 5" <<endl;
    x = 5;
    cout << "x = " << x << " | x_ref = " << x_ref <<endl<<endl;

    cout << "Changing x_ref to 3" <<endl;
    x_ref = 3;
    cout << "x = " << x << " | x_ref = " << x_ref <<endl<<endl;

    cout << "------------------------------" <<endl<<endl;

    int a = 5;
    int b = 7;
    cout << "a = " << a << " | b = " << b <<endl<<endl;

    cout << "Swapping a and b" <<endl;
    swap(a, b);
    cout << "a = " << a << " | b = " << b <<endl<<endl;

    return 0;
}