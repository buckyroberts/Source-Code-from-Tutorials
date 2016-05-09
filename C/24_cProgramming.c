#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a = 5, b = 10, answer = 0;
	printf("The first a = %d \n", a);	
	
	// add one to a immediately
	answer = ++a * b;
	
	printf("Answer: %d \n", answer);
	printf("The second a = %d \n", a);

	a = 5, b = 10, answer = 0;
	printf("\nThe reset a = %d \n", a);
	
	answer = a++ * b;
	// add one after running code
	
	printf("Answer: %d \n", answer);
	printf("The last a = %d \n", a);

	return 0;
}
