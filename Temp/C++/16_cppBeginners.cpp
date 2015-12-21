#include <iostream>
using namespace std;

int main()
{
    int x = 10;
    int y = 43;

    if (x == 10){ // 10 equals 10 - true
        cout << "omg i am preggy" << endl;
    }

    if (x != 87){ // 10 is not equal to 87 - true
        cout << "omg i am preggy" << endl;
    }

    if (x < 87){ // is 10 less than 87? - true
        cout << "omg i am preggy" << endl;
    }

    if (x > 87){ // is 10 greater than 87? - false
        cout << "omg i am preggy" << endl;
    }

    if (x <= 10){ // is 10 less than or equal to 10? - true
        cout << "omg i am preggy" << endl;
    }

    if (x >= y){ // is 10 greater than or equal to 43 - false
        cout << "omg i am preggy" << endl;
    }

    return 0;
}
