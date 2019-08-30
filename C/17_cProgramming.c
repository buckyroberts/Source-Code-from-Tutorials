#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age;

    printf("How old are you? \n");
    scanf("%d", &age);

    if(age >= 18){
        printf("You may enter this website!");
    }

    if(age < 18){
        printf("Nothing to see here!");
    }

    return 0;
}

