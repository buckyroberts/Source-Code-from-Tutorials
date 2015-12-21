#include <iostream>

using namespace std;

// This function takes two parameters.
int addNumbers(int x, int y){
    int answer = x + y;
    return answer;
}

int main()
{
    cout << addNumbers(43, 86); // Call the function.

    return 0;
}

