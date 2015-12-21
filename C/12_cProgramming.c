
// Math in statements, floats.  Code modified a bit

#include <stdio.h>
#include <stdlib.h>


int main()
{

    int weight = 595;
    printf("I weigh %d lbs. \n", weight + 12);
    printf("I weigh %d lbs. \n", weight / 12);
    printf("I weigh %d lbs. \n\n", weight % 12);

    int a = 86;
    int b = 21;

    printf("%d \n", a/b);

    float c = 86.0;
    float d = 21.0;
    printf("%f \n", c/d);

    return 0;
}
