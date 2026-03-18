#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}node;

void unload(node *list); // i must let unload know node before

int main(void)
{
    // Memory for numbers
    node *list = NULL;
    // Build list
    for (int i = 0 ; i<3 ; i++)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            unload(list);
            return 1;
        }
        //create a single n
        n->number = get_int("Number: ");
        n->next = NULL;
        if (list == NULL)//list is empty
        {
            list = n;
        }
        else if (n->number < list->number)// if n is 1 and list is 23
        {
            n->next = list;
            list = n;
        }
        else
        {
            for (node *ptr =list ; ptr!=NULL ; ptr = ptr->next)//create a new variable to compare n and temporary's number
            {
                if (ptr->next == NULL)
                {
                    ptr->next = n;
                    break;
                }
                if(n->number < ptr->next->number)//if ptr->next is NULL,it couldn't have a number so when i have 124 3 want to insert before 4 however 4->next is NULL error would happen so i must let ptr->next == NULL be juadged first
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;//prevent the loop
                }
            }
        }
    }
    // Print numbers
    for (node *ptr = list ; ptr!=NULL ; ptr = ptr->next)
    {
        printf("%i\n",ptr->number);
    }
    unload(list);
    return 0;
}

//free memory
void unload(node *list)
{
    node *ptr = list; //list is the pointer i let ptr become list
    while (ptr!=NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
}
