// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool lower = false;
    bool upper = false;
    bool number = false;
    bool symbol = false;

    int length = strlen(password);
    if (length < 8)
    {
        return false;
    }
    for (int i = 0; i < length; i++)
    {
        if (isupper(password[i]))
        {
            upper = true;
        }
        if (islower(password[i]))
        {
            lower = true;
        }
        if (isdigit(password[i]))
        {
            number = true;
        }
        if (ispunct(password[i]))
        {
            symbol = true;
        }
    }
    return (lower && upper && number && symbol);
}
