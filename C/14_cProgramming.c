
// Moar math.

#include <stdio.h>
#include <stdlib.h>


int main()
{

    float age1, age2, age3, average;

    printf("Enter your age of 1st person\n");
    scanf("%f", &age1);
    printf("Enter your age of 2nd person\n");
    scanf("%f", &age2);
    printf("Enter your age of 3rd person\n");
    scanf("%f", &age3);

    average = (age1 + age2 + age3) / 3;
    printf("\n The average age of the group is %f", average);

    return 0;
}
