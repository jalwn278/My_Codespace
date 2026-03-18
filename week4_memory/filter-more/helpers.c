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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
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
            float Gx_r = 0;
            float Gy_r = 0;
            float Gx_g = 0;
            float Gy_g = 0;
            float Gx_b = 0;
            float Gy_b = 0;
            int gx[3][3] = {
                {-1, 0, 1},
                {-2, 0, 2},
                {-1, 0, 1}};

            int gy[3][3] = {
                {-1, -2, -1},
                {0, 0, 0},
                {1, 2, 1}};
            for (int r = -1 ; r <= 1; r++)
            {
                for (int n = -1; n <= 1; n++)
                {
                    int coordinate_y = i + r;
                    int coordinate_x = j + n;
                    if (coordinate_y >= 0 && coordinate_y < height && coordinate_x >= 0 && coordinate_x < width)
                    {
                         Gx_r += temp[coordinate_y][coordinate_x].rgbtRed*gx[r+1][n+1];
                         Gy_r += temp[coordinate_y][coordinate_x].rgbtRed*gy[r+1][n+1];
                         Gx_g += temp[coordinate_y][coordinate_x].rgbtGreen*gx[r+1][n+1];
                         Gy_g += temp[coordinate_y][coordinate_x].rgbtGreen*gy[r+1][n+1];
                         Gx_b += temp[coordinate_y][coordinate_x].rgbtBlue*gx[r+1][n+1];
                         Gy_b += temp[coordinate_y][coordinate_x].rgbtBlue*gy[r+1][n+1];
                    }
                }
            }
            int red = round(sqrt(Gx_r*Gx_r + Gy_r*Gy_r));
            int green = round(sqrt(Gx_g*Gx_g + Gy_g*Gy_g));
            int blue = round(sqrt(Gx_b*Gx_b + Gy_b*Gy_b));
            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}
