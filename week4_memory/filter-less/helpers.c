#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtBlue+image[i][j].rgbtGreen+image[i][j].rgbtRed)/3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float originalRed = image[i][j].rgbtRed;
            float originalGreen = image[i][j].rgbtGreen;
            float originalBlue = image[i][j].rgbtBlue;

            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            int sepia[3]={sepiaRed, sepiaGreen, sepiaBlue};

            for (int n = 0; n < 3; n++)
            {
                if (sepia[n] > 255)
                sepia[n] = 255;
            }

            image[i][j].rgbtRed = sepia[0];
            image[i][j].rgbtBlue = sepia[2];
            image[i][j].rgbtGreen = sepia[1];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2 ; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width-1-j];
            image[i][width-1-j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++) //genius input first i get every image[i][j] and make image[i][j] as 0 up and left is -1 down and right is +1 if (i+r) >= 0 and < height it counts if (j+n)>=0 and < width it counts
    {
        for (int j = 0; j < width; j++)
        {
            float totalred = 0;
            float totalgreen = 0;
            float totalblue = 0;
            float count = 0;
            for (int r = -1 ; r <= 1; r++)
            {
                for (int n = -1; n <= 1; n++)
                {
                    int coordinate_y = i + r;
                    int coordinate_x = j + n;
                    if (coordinate_y >= 0 && coordinate_y < height && coordinate_x >= 0 && coordinate_x < width)
                    {
                        totalred += temp[coordinate_y][coordinate_x].rgbtRed;
                        totalgreen += temp[coordinate_y][coordinate_x].rgbtGreen;
                        totalblue += temp[coordinate_y][coordinate_x].rgbtBlue;
                        count++;
                    }
                }
            }
            image[i][j].rgbtRed = round(totalred / count);
            image[i][j].rgbtGreen = round(totalgreen / count);
            image[i][j].rgbtBlue = round(totalblue / count);
        }
    }
    return;
}
