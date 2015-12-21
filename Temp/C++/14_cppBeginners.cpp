#include <iostream>
#include <string>
using namespace std;

class BuckysClass{
    public:
        BuckysClass(string z){
            setName(z);
        }
        void setName(string x){
            name = x;
        }
        string getName(){
            return name;
        }
    private:
        string name;
};


int main()
{
    BuckysClass bo("Lucky Bucky roberts");
    cout << bo.getName();

    BuckysClass bo2("Sally mcSalad");
    cout << bo2.getName();
    return 0;
}
