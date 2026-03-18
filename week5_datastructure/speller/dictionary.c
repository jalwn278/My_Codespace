// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;
int total = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int num = hash(word);

    node *ptr = table[num];
    while (ptr != NULL)
    {
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int c0 = 0, c1 = 0, c2 = 0;
    if(isalpha(word[0]))
    {
        c0 = toupper(word[0]) - 'A';
    }

    if (word[1] != '\0')
    {
        c1 = toupper(word[1]) - 'A';

        if (word[2] != '\0')
        {
            c2 = toupper(word[2]) - 'A';
        }
    }
    return (c0*26*26) + (c1*26) + c2;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    FILE *source = fopen(dictionary,"r");
    if (source == NULL)
    {
        return false;
    }

    char word[LENGTH+1];
    int index = 0;

    while (fscanf(source,"%s",word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        index = hash(word);
        n->next = table[index];
        table[index] = n;

        total++;
    }
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return total;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *temp = table[i];
        while (temp != NULL)
        {
            node *p = temp->next;
            free(temp);
            temp = p;
        }
    }
    return true;
}
