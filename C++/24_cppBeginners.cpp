#include <iostream>
using namespace std;

int main()
{

    int x = 99;

    do{     // will run at least one time
        cout <<x<<endl;
        x++;
    }while(x<10); // test is false

}
// do-while loop is different from while loop as in while loop, the condition is check first and then the further
// statements are executed, while in do-while loop, firstly the statements are executed and then the condition is checked.
// So, do-while loop will always be executed at least one time.
