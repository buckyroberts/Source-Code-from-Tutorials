#include <stdio.h>
#include <stdlib.h>

int main()
{
	float grade1;
	float grade2;
	float grade3;

	printf("Enter your 3 test grades: \n");
	scanf(" %f", &grade1);
	scanf(" %f", &grade2);
	scanf(" %f", &grade3);

	float avg = (grade1 + grade2 + grade3) / 3;
	printf("Average: %.2f \n", avg);	

	if(avg >= 90) {
	    printf("Grade: A\n");
	}else if(avg >= 80) {
	    printf("Grade: B\n");
	}else if(avg >= 70) {
	    printf("Grade: C\n");
	}else{
	    printf("You are dumb!\n");
	}

	return 0;
}
