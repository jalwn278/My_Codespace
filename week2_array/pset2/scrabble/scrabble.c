#include <string.h>
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int compute_scores(string verb);

int main(void)
{
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    int scores_p1 = compute_scores(p1);
    int scores_p2 = compute_scores(p2);

    if (scores_p1 > scores_p2)
    {
        printf("Player 1 wins!\n");
    }
    else if (scores_p2 > scores_p1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

}

int compute_scores(string verb)
{
     //array中的值不同写作array[]={1,2,....}
    int scores[]={1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int sum = 0;
    for (int i = 0 , n = strlen(verb) ; i<n ; i++)
    {
        char c = toupper(verb[i]);  //在 char c 下设有循环，这样子就不用构造列表了

        if (c>='A' && c<='Z')//要用ASCII码需要'A'
        {
            int point = c-'A';
            sum += scores[point];
        }
    }
}
