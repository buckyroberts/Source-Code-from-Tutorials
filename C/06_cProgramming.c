#include <stdio.h>
#include <stdlib.h>

int main() {
	
	//will replace %s with bucky
	printf("%s is best person ever \n", "Bucky");
	
	//will replace %d with 9
	printf("I ate %d corndogs last night \n", 9);
	
	//will replace %f with 3.14159 
	printf("Value of pi is %f \n", 3.14159);
	
	//will replace %f with 3.14 (2 decimal) 
	printf("Value of pi is %.2f \n", 3.14159);
	
	//will replace %f with 3.14159  (3 decimal
	printf("Value of pi is %.3f \n", 3.14159);
	
	return 0;
}