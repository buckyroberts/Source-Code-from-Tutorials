#include <stdio.h>
#include <stdlib.h>

int main() {
	
	//Computer adds \0 to the end of string to know that
	//Its the end of that string
	//Its called string terminator
	
	
	//Array of character of length 14
	char name[14] = "Bucky Roberts";
	printf("My name is %s \n", name);
	
	return 0;
}