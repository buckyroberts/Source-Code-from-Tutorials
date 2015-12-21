//This is Sally.h file
#ifndef SALLY_H
#define SALLY_H

class Sally
{
	public:
		Sally();
		void printCrap();
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
}
void Sally::printCrap(){
	cout<< "did someone say steak?"<<endl;
}

//This is main cpp.
#include <iostream>
#include "Sally.h"
using namespace std;

int main(){
	Sally sallyObject;
	Sally *sallyPointer = &sallyObject;
	
	sallyObject.printCrap();
	sallyPointer->printCrap();
}