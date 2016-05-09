#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>



int main()
{
	char a = 'a';
	char b = 'F';
	char c = '7';

	printf("%c \n", toupper(a));
	printf("%c \n", toupper(b));
	printf("%c \n", toupper(c));

	/*
	char ham[100] = "Hey ";

	strcat(ham, "Bucky ");
	strcat(ham, "you ");
	strcat(ham, "smell! ");
	printf("%s \n", ham);

	strcpy(ham, "Bucky is Awesome!");
	printf("%s \n", ham);
	*/
	return 0;
}
