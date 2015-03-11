#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	 ofstream buckyFile;
	 buckyFile.open("tuna.txt");
	 
	 buckyFile << "I love tuna and tuna loves me!\n";
	 buckyFile.close();
}