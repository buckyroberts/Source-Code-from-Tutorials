//This is Hannah.h file
#ifndef HANNAH_H
#define HANNAH_H

class Hannah{
	
		public:
			Hannah(int);
			void printCrap();
		private:
			int h;	
};
//This is Hannah.cpp file
#include <iostream.h>
#include "Hannah.h"
using namespace std;

Hannah::Hannah(int num)
:h(num)
{
}

void Hannah::printCrap(){
	cout << "h=" << h <<endl;
	cout << "this->h=" << this->h <<endl;
	cout << "(*this).h=" << (*this).h <<endl;
}
//This is main.cpp file
#include <iostream>
#include "Hannah.h"
using namespace std;

int main(){
	Hannah ho(23);
	ho.printCrap();
}