#include <iostream>
using namespace std;

int main()
{
    int bucky[9];

    cout << "Element  -  Value" << endl;
    for (int x= 0; x<=8; x++){
        bucky[x] = 99;
        cout << x << "   -----   " << bucky[x] << endl;
    }
}
