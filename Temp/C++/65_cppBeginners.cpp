#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	 ofstream buckysFile("beefjerky.txt");
	 
	 if(buckysFile.is_open()){
		cout  << "okt he file is open" <<endl;
		}else(
			cout << "bucky you messed up" << endl;
		)

	 buckysFile << "oi love the beef!\n";
	 buckysFile.close();
}