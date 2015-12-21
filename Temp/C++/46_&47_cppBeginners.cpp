//This is Birthday.h file
#ifndef BIRTHDAY_H
#define BIRTHDAY_H

class Birthday
{
	public:
		Birthday(int m, int d,int y);
		void printDate();
    private:
		int month;
		int day;
		int year;
};

#endif // BIRTHDAY_H

//This is Birthday.cpp file
#include "Birthday.h"
#include <iostream>
using namespace std;

Birthday::Birthday(int m, int d, int y)
{
	month = m;
	day = d;
	year = y;
}

void Birthday::printDate(){
	cout << month << "/" << day << "/" << year <<endl;
}

//This is People.h file
#ifndef PEOPLE_H
#define PEOPLE_H

#include <string>
#include "Birthday.h"
using namespace std;

class People
{
	public:
		People(string x,Birthday bo);
		void printInfo();
	private:
		string name;
		Birthday dataOfBirth;
};

#endif // PEOPLE_H

//This is People.cpp file
#include "People.h"
#include "Birthday.h"
#include <iostream>
using namespace std;

People::People(String x,Birthday bo)
: name(x), dataOfBirth(bo)
{
}

void People::printInfo(){
	cout << name << "was born on";
	dataOfBirth.printDate();
}
//This is main.cpp file
#include <iostream>
#include "Birthday.h"
#include "People.h"
using namespace std;

int main()
{
	Birthday birthObj(12,28,1986);
	
	People buckyRoberts("Bucky the King",birthObj);
	buckyRoberts.printInfo();
	
}