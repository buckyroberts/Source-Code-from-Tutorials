#include <iostream>
using namespace std;

int main()
{
    int tuna[5] = {20,54,76,832,546};
    int sum = 0;

    for(int x = 0; x < 5; x++){
        sum += tuna[x];
        cout << sum << endl;
    }
}
