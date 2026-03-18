#include <stdio.h>
#include <cs50.h>

void print_ladder(int space, int hash);

int main(void)
{
    int height;
    do{
        height = get_int("Height: ");
    }while(height < 1 || height > 8);

    for (int i = 0; i < height; i ++)
    {
        int space = height - 1 - i;
        int hash = i + 1;
        print_ladder(space, hash);
    }
}

void print_ladder(int space, int hash)
{
    for (int j = 0 ; j < space; j++)
    {
        printf(" ");
    }
    for (int j = 0; j < hash; j++)
    {
        printf("#");
    }
    printf("  ");
    for (int j = 0; j < hash; j++)
    {
        printf("#");
    }
    printf("\n");
}
