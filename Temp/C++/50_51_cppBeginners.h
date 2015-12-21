//This is Sally.h file
#ifndef SALLY_H
#define SALLY_H

class Sally
{
	public:
		int num;
		Sally();
		Sally(int);
		Sally operator+(Sally);
}
//This is Sally.cpp file
#include <iostream>
#include "Sally.h"
using namespace std;

Sally::Sally()
{	
}

Sally::Sally(int a){
	num = a;
}
Sally Sally::operator+(Sally aso){
	Sally brandNew;
	brandNew.num = num + aso.num;
	return(brandNew);
}
//This is main.cpp file
#include <iostream>
#include "Sally.h"
using namespace std;

int main()
{
	Sally a(34);
	Sally b(21);
	Sally c;
	c=a+b;
	cout << c.num << endl;
	
}
