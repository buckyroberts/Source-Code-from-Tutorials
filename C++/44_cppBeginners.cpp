//This is Sally.h file
#ifndef SALLY_H
#define SALLY_H

class Sally
{
	public:
		Sally();
		void printShiz();
		void printShiz2() const;
	protected;
	private;
};

#endif //SALLY_H

//This is Sally.cpp file
#include "Sally.h"
#include <iostream>
using namespace std;

Sally::Sally()
{	
}

void Sally::printShiz()
{
	cout << "i am a regular function"<<endl;
}

void Sally::printShiz2() const{
	cout<< "i am the constant function"<<endl;
}

//This is main.cpp file
#include <iostream>
#include "Sally.h"
using namespace std;

int main(){
	Sally salObj;
	salObj.printShiz();
	
	const Sally constObj;
	constObj.printShiz2();
}