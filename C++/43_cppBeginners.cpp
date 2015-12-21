//This is Sally.h file
#ifndef SALLY_H
#define SALLY_H

class Sally
{
	public:
		Sally();
		~Sally();
		protected:
		private:
};
#endif // SALLY_H

//This is Sally.cpp file
#include "Sally.h"
#include <iostream>
using namespace std;

Sally::Sally()
{	
	cout<< "i am the constructor" << endl;
}

Sally::~Sally()
{	
	cout<< "i am the deconstructor" << endl;
}

//This is main.cpp file
#include <iostream>
#include "Sally.h"
using namespace std;

int main(){
	
	Sally so;
	cout << "omg wtf is this on my shoe? "<<endl;
}