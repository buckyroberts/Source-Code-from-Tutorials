#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>



int main()
{
	char grade = 'C';
	// char grade = 'P';
	// char grade = 'B';

	switch(grade) {
	    case 'A': printf("SWEAT! \n");
		break;
	    case 'B': printf("Could have tried harder \n");
		break;
	    case 'C': printf("I C you didn't study \n");
		break;
	    case 'D': printf("You love the D \n");
		break;
	    case 'F': printf("That's embarrassing \n");
		break;
	    default: printf("That doesn't even make sense! \n");
	}

	return 0;
}
