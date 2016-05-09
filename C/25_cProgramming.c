#include <stdio.h>
#include <stdlib.h>

int main()
{
	int day = 1;
	float amount = .01;

	while(day <= 31) {
	    printf("Day: %d \t Amount: $%.2f \n", day, amount);
	    amount *= 2;
	    day++;
	}

	return 0;
}
