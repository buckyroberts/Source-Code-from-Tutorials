
// Order of operations

#include <stdio.h>
#include <stdlib.h>


int main()
{

    int a = 4 + 2 * 6;
    printf("Result: %d \n", a);
    a = (4 + 2) * 6;
    printf("Result: %d \n", a);

    return 0;
}
