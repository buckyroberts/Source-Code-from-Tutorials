#include <iostream>
using namespace std;

int main()
{

    int a = 10, b = 10, c = 10, d = 10, e = 10, x;

    a += 5; // is the same as a = a + 5;
    cout << a << endl;

    b -= 5; // is the same as b = b - 5;
    cout << b << endl;

    c *= 5; // is the same as c = c * 5;
    cout << c << endl;

    d /= 5; // is the same as d = d / 5;
    cout << d << endl;

    e %= 3; // is the same as e = e % 3; Modulus Operator (%) - divides the values and than returns the remainder - 10 % 3 = 1
    cout << e << endl;


    // increment operators
    x = 20;
    cout << x++ << endl; // first it prints the value than it will increment x - 20
    cout << x << endl; // 21

    x = 20;
    cout << ++x << endl; // increments first and than it will print the value of x - 21
    cout << x << endl; // 21

    x = 20;
    cout << x-- << endl; // first it prints the value than it will decrement x - 20
    cout << x << endl; // 19

    x = 20;
    cout << --x << endl; // decrement first and than it will print the value of x - 19
    cout << x << endl; // 19

}
