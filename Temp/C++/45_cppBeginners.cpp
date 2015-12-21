//This is Sally.h file
#ifndef SALLY_H
#define SALLY_H

class Sally
{
	public:
		Sally(int a,int b);
		void print();
	private:
		int regVar;
		const int constVar;
};

#endif //SALLY_H

//This is Sally.cpp file
#include "Sally.h"
#include <iostream>
using namespace std;

Sally::Sally(int a,int b)
:regVar(a),
constVar(b)
{	
}

void Sally::print(){
	cout << "regular var is: " << regVar << "const varible is :" << constVar <<endl;
}
//This is main.cpp file
#include <iostream>
#include "Sally.h"
using namespace std;

int main()
{
	Sally so(3,87);
	so.print();
}