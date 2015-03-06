#include <iostream>
#include <cmath> // include cmath library
using namespace std;

int main()
{

    float a; // amount
    float p = 10000; // principal amount - start amount
    float r = .03; // interest rate

    for (int day = 1; day <=30; day++){
        a = p * pow(1+r, day);
        cout << day << " ----- " << a << endl;
    }
}
