#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number; //stored data
    struct node *next; // the address of storing next box
}node;

int main(void)
{
    node *list = NULL; // arrows's edge

    for (int i = 0 ; i<3 ; i++)
    {
        node *n = malloc(sizeof(node)); //temporary n
        if (n == NULL) // if n!= NULL means node *n = malloc(sizeof(node)) is successful
        {
            return 1;
        }
        (*n).number = get_int("Number: "); //n->number = get_int("Number: "); put number into n
        (*n).next = NULL; // n->next = NULL; n heading to nothing

        //add new node at the start of the list (prepend node to the list)
        n->next = list;// if n is first it heading to NULL if n is second it heading to first
        list = n;//update list let the newest n put arrow's tail
    }

    for (node *ptr = list ; ptr != NULL ; ptr = ptr->next)
    {
        printf("%i\n",ptr->number);
    }

    /*node *ptr = list;
    while (ptr != NULL)
    {
        printf("%i\n",ptr->number);
        ptr = ptr->next; // it will print 30 20 10 if i input 10 20 30
    }*/

    return 0;
}
