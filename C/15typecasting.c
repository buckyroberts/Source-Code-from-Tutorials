#include <stdio.h>
#include <stdlib.h>

int main()
{
    //typecasting
    float avgProfit;
    int priceOfItem = 60;
    int sales = 500;
    int daysWorked = 7;

    //if you try to do math with ints and floats mixed, it will not be precise, so...
    //use (float) before int variable - casts int as float for just that line, then goes back to int
    avgProfit = ( (float)priceOfItem * (float)sales) / (float)daysWorked;
    printf("Average daily profit: $%.2f", avgProfit);

    return 0;

}
