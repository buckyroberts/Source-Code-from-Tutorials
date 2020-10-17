#include <stdio.h>
#include <stdlib.h>

int main() {
	
	int age;
	int currentYear;
	int birthYear;
	
	printf("Enter Current Year");
        scanf("%d",&currentYear);
	birthYear = 1987;
	age = (currentYear - birthYear);
	
	printf("Bucky is %d years old \n", age);
	
	return 0;
}