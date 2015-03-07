#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	
	float age1, age2, age3, average;
	age1 = age2 = 4;
	
	printf("Enter your age? \n");
	scanf("%f", &age3);
	
	average = (age1 + age2 + age3) / 3;
	printf("The average of group is %f \n", average);
	return 0;
}