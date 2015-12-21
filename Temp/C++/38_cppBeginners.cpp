#include <iostream>
using namespace std;

int main(){
    int fish = 5;
    cout << &fish << endl; // address operator (&)

    int *fishPointer; // a pointer
     fishPointer = &fish;

     cout << fishPointer << endl;
}
