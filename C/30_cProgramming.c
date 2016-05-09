#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>



int main()
{
	int num = 1;

	do{
	    if(num == 6 || num == 8) {
		num++;
		continue;
	    }

	    printf("%d is available \n", num);
	    num++;

	}while(num <= 10);

	return 0;
}
