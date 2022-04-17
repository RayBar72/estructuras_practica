#include "main.h"

void times_table(void)
{
    int num = 1, i = 0, j = 0, dc = 0, un = 0, n = 0;

    for(i = 0; i <= 9; i++)
    {
        for(j = 0; j <= 9; j++)
        {
            n = (num * j) * i;
            dc = n / 10;
            un = n % 10;
            if (j != 0)
            {
                putchar(',');
                putchar(' ');
                if (dc == 0)
                    putchar(' ');
                if (dc != 0)
                    putchar(dc + '0');
                putchar(un + '0');
                if (j == 9)
                    putchar('\n');
            }
            if (j == 0)
                putchar('0');
        }
    }
}