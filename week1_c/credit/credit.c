#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long number;
    do{
        number = get_long("Number: ");
    }while(number <= 0);

    long temp_number = number;
    int length = 0;
    int array[16]={0}; //prevent trash value

    for (int i = 0; i < 16; i++)
    {
        if (temp_number > 0)
        {
            array[i]=temp_number % 10;
            temp_number = temp_number / 10;
            length +=1;
        }
    }

    int total_1 = 0;
    for (int i = 1 ; i < 16; i+=2)
    {
        int number_double = array[i]*2;
        if (number_double >= 10)
        {
            number_double = number_double - 9;
        }
        total_1 += number_double; //total_1 = (d/10)+(d%10);
    }

    int total_2 = 0;
    for (int i = 0; i < 16; i+=2)
    {
        total_2 += array[i];
    }

     int total = total_1 + total_2;

     if (total % 10 != 0)
     {
        printf("INVALID\n");
        return 0;
     }

     int firsttwo = array[length-1]*10 + array[length-2];
     int firstone = array[length-1];

     if (length == 15 && (firsttwo == 34 || firsttwo == 37))
     {
        printf("AMEX\n");
     }

     else if (length == 16 && (firsttwo >= 51 && firsttwo <= 55))
     {
        printf("MASTERCARD\n");
     }

     else if ((length == 13 || length ==16) && firstone == 4)
     {
        printf("VISA\n");
     }
     else
     {
        printf("INVALID\n");
     }
}
