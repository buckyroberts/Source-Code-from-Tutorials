//This is Mother.h file
#ifndef MOTHER_H
#define MOTHER_H

class Mother
{
	public:
		int publicv;
	protected:
		int protectedv;
    private:
		int privatev;
};

#endif // MOTHER_H

//This is Mother.cpp file
#include <iostream.h>
#include "Mother.h"
#include "Daughter.h"
using namespace std;

//This is Daughter.h file
#ifndef DAUGHTER_H
#define DAUGHTER_H

class Daughter: public Mother
{
	public:
		void dosomething();
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
	tina.dosomething();
}
 