#include <iostream>
using namespace std;

template <class bucky>
bucky addCrap(bucky a, bucky b)
{
return a+b;
}

int main()
{
	int x=7, y=43,z;
	z=addCrap(x,y);
	cout << z <<endl;
}