#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int calculate(string n);

int main(void)
{
    string word_1 = get_string("Player 1: ");
    string word_2 = get_string("Player 2: ");

    int score_1 = calculate(word_1);
    int score_2 = calculate(word_2);

    if (score_1 > score_2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score_1 < score_2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int calculate(string n)
{
    int array[26]={1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int length = strlen(n);

    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        if (isalpha(n[i]))
        {
            char letter = toupper(n[i]);
            if (letter >= 'A' && letter <= 'Z')
            {
                int value = letter - 'A';
                sum += array[value];
            }
        }
    }
    return sum;
}
