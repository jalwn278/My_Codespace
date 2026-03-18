#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("FILE couldn't be opened");
        return 1;
    }

    uint8_t buffer[512];

    int count = 0;
    char FILENAME[8];
    FILE *image = NULL;
    while(fread(buffer, 1, 512, f) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (image != NULL)
            {
                fclose(image);
            }

            sprintf(FILENAME, "%03i.jpg", count);
            image = fopen(FILENAME, "w");
            count++;
        }

        if (image != NULL)
        {
            fwrite(buffer, 1, 512, image); //byte is transported by buffer so they can be written in different if. If it's not passed by buffer it can't be writen like this
        }
    }

    if (image != NULL)
    {
        fclose(image);
    }
    fclose(f);

    return 0;
}
