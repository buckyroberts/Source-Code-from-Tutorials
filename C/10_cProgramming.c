

// Shows how values defined in header file work.

#include <stdio.h>
#include <stdlib.h>
#include "Buckysinfo.h"

int main()
{
    int girlsAge = (AGE / 2) + 7;
    printf("%s can date girls age %d or older.\n", MYNAME, girlsAge);
    return 0;
}
