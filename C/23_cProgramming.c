#include <stdio.h>
#include <stdlib.h>

int main()
{
	int friends = 87;
	// int friends = 1;

	printf("I have %d friend%s\n", friends, (friends != 1) ? "s" : "");

	return 0;
}
