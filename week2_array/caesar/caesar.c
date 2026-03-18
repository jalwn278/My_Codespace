#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc , string argv[])
{
    if (argc!=2)
    {
        printf("Usage: ./caeser key\n");
        return 1;
    }
    for (int i = 0 , n = strlen(argv[1]) ; i<n ; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caeser key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);

    string input = get_string("plaintext: ");
    char ciphertext[strlen(input) + 1];

    for(int i = 0 ,n = strlen(input) ; i<n ; i++)
    {
        char c = input[i];//获取input中第i个
        if (isalpha(c))
        {
            if (isupper(c))
            {
                ciphertext[i]='A' + (c - 'A' + key) % 26;//后者把它放在0~25进行计算再加上'A'变回大写
            }
            else
            {
                ciphertext[i]='a' + (c - 'a' + key) % 26;
            }
        }
        else
        {
            ciphertext[i] = c;
        }
    }

    ciphertext[strlen(input)] = '\0';

    printf("Ciphertext: %s\n", ciphertext);
    return 0;
}
