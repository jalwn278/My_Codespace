#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int hash(char *word);
int main(void)
{
    char *word = get_string("Word: ");
    printf("Hash value: %i\n" , hash(word));
}

int hash(char *word)
{
    if (word == NULL || strlen(word) == 0)
    {
        return -1;
    }
    char c = word[0];
    if (isalpha(c))
    {
        c = toupper(c);
        return c-'A';
    }
    return -1;
}
