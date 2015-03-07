#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	
	char firstName[20];
	char crush[20];
	int numberOfBabies;
	
	//Using scanf to get user Input 
	printf("What is your name?\n");
	scanf("%s", &firstName);
	
	printf("Who you gonna get marry to? \n");
	scanf("%s", &crush);
	
	printf("How many kids will you have? \n");
	scanf("%d", &numberOfBabies);
	
	printf("%s and %s are in love and have %d babies \n", firstName, crush, numberOfBabies);
	return 0;
}