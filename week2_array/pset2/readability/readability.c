#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count(string s);

int main(void)
{
    string text = get_string("Text: ");

    int grade = count(text);

    if (grade<1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade>=16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n",grade);
    }
}

int count(string s)
{
    int index = 0;
    int letter = 0;
    int sentences = 0;
    int words = 0;
    int length =strlen(s);

    for (int i = 0  ; i<length ; i++)
    {
        if (isalpha(s[i])) //isalpha判断是不是字母
        {
            letter++;
        }

        if (s[i] == ' ')
        {
            words++;
        }

        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            sentences++;
        }
    }

    double L = (double)letter * 100 / words ; //每一百单词的平均数
    double S = (double)sentences * 100 / words ;

    index = (int)round(0.0588 * L - 0.296 * S - 15.8);
    return index; //要返回到主函数
}
