#include <climits>
#include <iostream>

using namespace std;

int main()
{
    int a;
    int b;
    int sum;
    
    cout << "Enter a number hoss! \n";
    cin >> a;
    if (!cin.good()) {
        cout << "That wasn't a number, wanker! \n";
        return 0;
    }
    
    cout << "Enter another number \n";
    cin >> b;
    if (!cin.good()) {
        cout << "That wasn't another number \n";
        return 0;
    }
    
    if ((a < 0 && b < 0 && INT_MIN - a > b) || (a > 0 && b > 0 && INT_MAX - a < b)) {
        cout << "the sum of those numbers would cause an error" << endl;
    }
    else {
        sum = a+b;
        cout << "the sum of those numbers is " << sum << endl;
    }
    return 0;
}
