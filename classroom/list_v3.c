#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}node;

int main(void)
{
    node *list = NULL;

    for (int i = 0 ; i<3 ; i++)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)  //fail to get memory
        {
            free(list);
            return 1;
        }
        n->number = get_int("Number: ");
        n->next = NULL;  //there is no number in list now so when list == NULL n could insert into list
        if (list == NULL) //list is empty
        {
            list = n;
        }
        else if (n->number < list->number)
        {
            n->next = list;
            list = n;//insert 1 before 2
        }
        else
        {
            for (node *ptr = list ; ptr != NULL ; ptr = ptr->next)
            {
                if (ptr->next == NULL )
                {
                    ptr->next = n;
                    break; //append at the end
                }
                if (n->number < ptr->next->number)// if ptr-> number is 2 n->next->number is 4 at that time n->number == 3 lower than ptr->next->number  , so i let n->next heading to ptr->next and then i let ptr->next heading to n so n insert between 2 and 4
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;
                }
            }
        }
    }

    for (node *ptr = list ; ptr != NULL ; ptr = ptr->next)
    {
        printf("%i\n",ptr->number);
    }

    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next; //when ptr is 1 next is 2 create next to store 1 and free 2 then make ptr = next(1)
        free(ptr);
        ptr = next;
    }

    return 0;
}
