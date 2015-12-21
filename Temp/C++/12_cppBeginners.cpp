#include <iostream>

using namespace std;

// Declare a class and define function inside the class
class BuckysClass{
    public: // You can use the function outside of the class.
        void coolSaying(){
            cout << "preachin to the choir" << endl;
        }

};

int main()
{
    BuckysClass buckysObject; // Create an object from BuckysClass
    buckysObject.coolSaying();
    return 0;
}
