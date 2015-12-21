// This is in a header file.  Go to "File" --> New -->
// Empty File, call it "Buckysroom.h"

// Done right, a headers folder should show up on CodeBlocks

# define MYNAME "Bucky"
# define AGE 28

//////////////////////////////////////////


// Shows how values defined in header file work.

#include <stdio.h>
#include <stdlib.h>
#include "Buckysinfo.h"

int main()
{
    int girlsAge = (AGE / 2) + 7;
    printf("%s can date girls age %d or older.", MYNAME, girlsAge);
    return 0;
}
