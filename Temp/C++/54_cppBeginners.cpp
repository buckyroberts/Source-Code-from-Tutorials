//This is Mother.h file
#ifndef MOTHER_H
#define MOTHER_H

class Mother
{
	public:
		Mother();
		~Mother();
};

#endif // MOTHER_H

//This is Mother.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

Mother::Mother(){
	cout<< "I am the mother constructor!" << endl;
}

Mother::~Mother(){
	cout<< "mother deconstructor!" << endl;
}
//This is Daughter.h file
#ifndef DAUGHTER_H
#define DAUGHTER_H

class Daughter: public Mother
{
	public:
		Daughter();
		~Daughter();
};

#endif // DAUGHTER_H

//This is Daughter.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

void Daughter::dosomething()
{
	publicv = 1;
	protected = 2;
}
//This is main.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

int main(){
		
	Daughter tina;

}
 