#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	 ifstream theFile("players.txt");
	 	 
	 int idNumber;
	 string name;
	 double money;
	 
	 while(theFile >> idNumber >> name >> money)
	 {
		cout <<idNumber << "," << name << "," << money << endl;
	 
	 }
	 
}
	 