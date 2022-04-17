#include "main.h"

void print_square(int size)
{
    int i = 0, n = size;

    if (size <= 0)
        putchar('\n');

    while (size)
    {
        for (i = 0; i < n; i++)
        {
            putchar('#');
        }
        putchar('\n');
        size--;
    }
}