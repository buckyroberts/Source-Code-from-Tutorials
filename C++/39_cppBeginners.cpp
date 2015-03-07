#include <iostream>
using namespace std;

void passByValue (int x);
void passByReference(int *x);

int main(){
    int betty = 13;
    int sandy = 13;

    passByValue(betty);
    passByReference(&sandy);

    cout << "betty is now " << betty << endl;
    cout << "sandy is now " << sandy << endl;
}

void passByValue (int x){
    x = 99;
}

void passByReference(int *x){
    *x=66;
}
