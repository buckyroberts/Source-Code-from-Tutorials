#include <iostream>
using namespace std;

int main()
{
    int age;
    int ageTotal = 0;
    int numberOfPeopleEntered = 0;

    cout << "Enter first persons age or -1 to quit" << endl;
    cin >> age;

    while(age != -1){
        ageTotal = ageTotal + age; // or shorthand: ageTotal += age;
        numberOfPeopleEntered++;

        cout << "Enter next persons age or -1 to quit" << endl;
        cin >> age;
    }

    cout << "Number of peoople eneted: " << numberOfPeopleEntered << endl;
    cout << "Average age: " << ageTotal/numberOfPeopleEntered;

    return 0;
}
