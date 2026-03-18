#include <stdio.h>
#include <cs50.h>

void print_ladder(int height);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: "); // if i define height in do-while the outside world couldn't receive height
    }while(height < 1);

    print_ladder(height);
}

void print_ladder(int height)
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 1; j < height - i; j++)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}
