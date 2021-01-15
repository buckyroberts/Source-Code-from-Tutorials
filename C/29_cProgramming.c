#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>



int main()
{
	int a;
	int howMany;
	int maxAmount = 10;

	printf("How many times do you want this loop to loop? (up to 10)\n");
	scanf(" %d", & howMany);

	for(a =1; a <= maxAmount; a++) {

	    printf("%d\n", a);

	    if(a == howMany) {
		break;
	    }

	}	
	return 0;
}
