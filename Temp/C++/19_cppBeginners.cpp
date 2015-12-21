#include <iostream>
using namespace std;

int main()
{
    int x = 1; // loop start point
    int number; // store the number the user enters
    int total = 0; // store the sum of the numbers

    while (x <= 5){
        cin >> number; // ask the user for a number and store it in the number variable
        total = total + number; // add the number to the total. HINT - the shorthand version is: total += number;
        x++; // is the same as: x = x + 1;
    }

    cout << "Your total is " << total << endl;

    return 0;
}
