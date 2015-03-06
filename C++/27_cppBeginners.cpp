#include <iostream>
#include <cstdlib> // include c standard library
#include <ctime> // to access the time of the computer
using namespace std;

int main()
{
    srand(time(0)); // seed random number from the clock

    for (int x = 1; x<25;x++){
        cout << 1+(rand()%6) << endl; // 6 <- the number of values you want to generate
    }

}
