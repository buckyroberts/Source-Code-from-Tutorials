#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	 ofstream theFile("players.txt");
	 
	 cout << "Enter palyers ID, Name, and Money" << endl;
	 cout << "press Ctrl+Z to quit\n" <<endl;
	 
	 int idNumber;
	 string name;
	 double money;
	 
	 while(cin >> idNumber >> name >> money)
	 {
	 theFile <<idNumber << ' ' << name << ' ' << money << endl;
	 
	 }
	 
}
	 