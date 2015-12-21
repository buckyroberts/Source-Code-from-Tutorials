#include <iostream>
using namespace std;
void bucky();

int tuna = 69; // global variable/global scope

int main()
{
    int tuna = 20; // local variable/local scope
    cout << tuna << endl; // local tuna
    cout << ::tuna << endl; // accessing global tuna using the unary scope resolution operator (::)

    bucky();
}

void bucky() { // bucky() can't access the tuna that is inside the main function
    cout << tuna << endl; // global tuna
}
