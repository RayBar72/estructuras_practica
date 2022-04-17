#include "main.h"

void more_numbers(void)
{
    int dec = 0, un = 0, num = 0, i = 14, j = 0;

    while (i)
    {
        for (j = 0; j <= 14; j++)
        {
            num = j;
            dec = num / 10;
            un = num % 10;
            if (dec != 0)
                putchar(dec + '0');
            putchar(un + '0');
        }
        i--;
        putchar('\n');
    }
}