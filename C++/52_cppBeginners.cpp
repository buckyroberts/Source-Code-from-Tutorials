//This is Mother.h file
#ifndef MOTHER_H
#define MOTHER_H

class Mother
{
	public:
		Mother();
		void sayName();
};

#endif // MOTHER_H

//This is Mother.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

Mother::Mother()
{
}

void Mother::sayName(){
	cout << "I am a RobnertsQ" << endl;
}

//This is Daughter.h file
#ifndef DAUGHTER_H
#define DAUGHTER_H

class Daughter: public Mother
{
	public:
		Daughter();
};

#endif // DAUGHTER_H

//This is Daughter.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

Daughter::Daughter()
{
}
//This is main.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

int main(){
		
	Daughter tina;
	tina.sayName();
}
