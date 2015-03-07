#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	
	// Order of math operation
	// First inside brackets
	// Then * or /
	// Then + or -
	
	int a = 4 + 2 * 6;
	
	printf("Result: %d \n", a);
	
	a = (4 + 2) * 6;
	printf("Result: %d \n", a);
		
	return 0;
}