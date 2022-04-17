#include "main.h"

void print_diagonal(int n)
{
    int i = 0, j = 0;

    if (n <= 0)
        putchar('\n');

    for (i = 0; i < n; i++)
    {
        for (j = 0; j <= i; j++)
        {
            if (i == j)
                putchar('\\');
            if (i != j)
                putchar(' ');
        }
        putchar('\n');
    }
}