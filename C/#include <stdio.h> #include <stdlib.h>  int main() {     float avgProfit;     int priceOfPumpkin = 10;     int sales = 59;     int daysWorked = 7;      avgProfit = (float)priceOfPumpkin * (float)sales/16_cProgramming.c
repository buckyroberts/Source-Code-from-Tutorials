#include <stdio.h>
#include <stdlib.h>

int main()
{
    float avgProfit;
    int priceOfPumpkin = 10;
    int sales = 59;
    int daysWorked = 7;

    avgProfit = (float)priceOfPumpkin * (float)sales / (float)daysWorked;
    printf ("Average Daily Profit: $%.2f", avgProfit);

    return 0;
}

