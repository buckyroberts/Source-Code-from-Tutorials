#include <stdio.h>
#include <stdlib.h>

int main() {
	
	int age;
	int currentYear;
	int birthYear;
	
	currentYear = 2014;
	birthYear = 1987;
	age = (currentYear - birthYear);
	
	printf("Bucky is %d years old \n", age);
	
	return 0;
}