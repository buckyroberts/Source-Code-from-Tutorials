#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>



int main()
{
	char ham[100] = "Hey ";

	strcat(ham, "Bucky ");
	strcat(ham, "you ");
	strcat(ham, "smell! ");
	printf("%s \n", ham);

	strcpy(ham, "Bucky is Awesome!");
	printf("%s \n", ham);
	
	return 0;
}
