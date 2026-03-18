// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char replacement(char i);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word");
        return 1;
    }

    int length = strlen(argv[1]);

    char output[length+1];

    for (int i = 0; i < length; i++)
    {
        char c = argv[1][i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o')
        {
            output[i] = replacement(c);
        }
        else
        {
            output[i] = c;
        }
    }


    output[length] = '\0';

    printf("%s\n",output);
}

char replacement(char i)
{
    switch (i)
    {
        case 'a':
            return '6';
        case 'e':
            return '3';
        case 'i':
            return '1';
        case 'o':
            return '0';
        default:
            return i;
    }
}
