#include <iostream>
using namespace std;

int main()
{
    int age = 178;

    if(age>60){
        cout << "wow you are old" << endl; // runs when the if statement is true

        if (age>100){ // a nested if statement
            cout << "why are you stil alive?" << endl; // this statement and the above statement runs when age > 100 is true.
        }                                              // so you get "wow you are old" and "why are you stil alive?" displayed on the screen.

    }else{
        cout << "you are young, get a job" << endl; // runs when the if statement is false
    }

    return 0;
}
