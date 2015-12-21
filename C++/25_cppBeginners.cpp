#include <iostream>
using namespace std;

int main()
{

    int age = 21;

    switch(age){
        case 16:
            cout << "hey you can drive now!" << endl;
            break; // end the case otherwise it will continue to run case 18, case 21 and default
        case 18:
            cout << "go buy some lotto ticekts~!" << endl;
            break; // end the case otherwise it will continue to run case 21 and default
        case 21:
            cout << "buy me some beer" << endl;
            break; // end the case otherwise it will continue and run default
        default:
            cout << "sorry you get nothign" << endl;
            // no break because it reached the end anyway.

    }

}
