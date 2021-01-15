#include <iostream>

using namespace std;

int main()
{
    int x = 81 /2; // Since we declare x to be an integer, x cannot be 40,5.

    cout << "x: " << x << endl; // So the result we get when we print x out is 40.

    int r = 81 % 2; // % Is called the modulus operator. It gives us the remainder of 81 divided by 2.

    cout << "r: " << r << endl; // It prints out the remainder r, which is 1 in this case.


    int calculation1 = 6 * 4 + 8 * 4 + 9 / 20; // It solves first multiplications and divisions and then sums it.
                                              //  So it gives us (6 * 4) + (8 * 4) + 9 / 20 = 24 + 32 + 0,45 = 56
                                             //   Since calculation1 is an integer, c++ ignores the decimal value 0,45
                                               

    int calculation2 = 4 + 3 * 7; // It gives us 4 + (3 * 7) = 25


    int calculation3 = (4 + 3) * 7; // calculation2 = 49
    
    
    int calculation4 = 2 + 6 * 3; // It gives us 2 + ( 6 * 3)= 20
    
    
    int calculation5 = (2 + 6) * 3;// calculaton5 = 24
    
    
    cout << "calculation1: " << calculation1 << endl;
    cout << "calculation2: " << calculation2 << endl;
    cout << "calculation3: " << calculation3 << endl;
    cout << "calculation4: " << calculation4 << endl;
    cout << "calculation5: " << calculation5 << endl;
    
    return 0;
}
