#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	
	char name[14] = "Bucky Roberts";
	printf("My name is %s \n", name);
	
	//changin 3rd element [Array index start from 0]
	name[2] = 'z';
	printf("My name is %s \n", name);
	
	char food[] = "tuna";
	printf("The best food is %s \n", food);
	
	//changing value of food by copying new value usinf strcpy function
	strcpy(food, "bacon");
	printf("The best food is %s \n", food);
	
	return 0;
}