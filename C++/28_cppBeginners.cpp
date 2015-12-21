#include <iostream>
using namespace std;

int volume(int l=1, int w=1, int h=1); // default values/parameters in function prototype

int main()
{
    cout << volume (5) << endl; // l=5, w=1, h=1 -> 5*1*1
}

int volume(int l, int w, int h){
    return l*w*h;
}
