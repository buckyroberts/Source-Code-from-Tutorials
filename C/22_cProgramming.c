#include <stdio.h>
#include <stdlib.h>

int main()
{
	char answer;
	
	printf("Do you like bagels? (y/n) \n");
	scanf(" %c", &answer);

	if( (5 < 90) || (10 == 10) ) {
	    printf("Good job, you didn't mess anything up\n");
	}else{
	    printf("Keyboard much?\n");
	}

	return 0;
}
