#include <iostream>
using namespace std;

int factorialFinder(int x){ // recursive function
    if(x==1){  // base case - end the function when x = 1
        return 1;
    }else{
        return x*factorialFinder(x-1);
    }
}

int main()
{
    cout << factorialFinder(5) << endl;
}
