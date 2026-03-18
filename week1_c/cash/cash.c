#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int coins = 0;
    int cash;

    do{
        cash = get_int("Change owed: ");
    }while(cash < 1);

    while (cash >= 25)
    {
        cash -= 25;
        coins++;
    }
    while (cash >= 10)
    {
        cash -= 10;
        coins++;
    }
    while (cash >= 5)
    {
        cash -= 5;
        coins++;
    }
    while (cash >=1)
    {
        cash -= 1;
        coins++;
    }

    printf("%i\n", coins);
}
