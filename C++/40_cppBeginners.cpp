#include <iostream>
using namespace std;

int main(){

    char a;
    cout << "size of char: " << sizeof(a) << endl;

    int b;
    cout << "size of int: " << sizeof(b) << endl;

    double c;
    cout << "size of double: "  << sizeof(c) << endl;
    
    long long int d;
    cout << "size of long long int: " << sizeof(d) << endl;
    
    float e;
    cout << "size of float: " << sizeof(e) << endl;

    double bucky[10];
    cout << "size of bucky[]: " << sizeof(bucky) << endl;
    cout << "no. of elements in bucky[]: " << sizeof(bucky) / sizeof(bucky[0]) << endl;

}
