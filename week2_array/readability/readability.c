#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

int letter(string n, int s);
int word(string n, int s);
int sentence(string n, int s);

int main(void)
{
    string text = get_string("Text: ");

    int length = strlen(text);
    int letters = letter(text, length);
    int words = word(text, length);
    int sentences = sentence(text, length);

    float L = (float)letters*100.0/words;
    float S = (float)sentences*100.0/words;
    int index = (int)round(0.0588*L - 0.296*S - 15.8);

    int level = index;

    if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (level >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", level);
    }
}


int letter(string n, int s)
{
    int number = 0;
    for (int i = 0 ; i < s; i++)
    {
        if (isalpha(n[i]))
        {
            number++;
        }
    }
    return number;
}

int word(string n, int s)
{
    int number = 1;
    for (int i = 0 ; i < s; i++)
    {
        if (n[i] == ' ')
        {
            number++;
        }
    }
    return number;
}

int sentence(string n, int s)
{
    int number = 0;
    for (int i = 0; i < s; i++)
    {
        if (n[i] == '.' || n[i] == '!' || n[i] == '?')
        {
            number++;
        }
    }
    return number;
}

