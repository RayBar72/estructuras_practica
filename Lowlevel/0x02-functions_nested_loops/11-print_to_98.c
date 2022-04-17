#include "main.h"

void print_to_98(int n)
{
    if (n == 98)
        puts("98");

    if (n < 98)
    {
        for(n; n < 98; n++)
            printf("%d, ", n);
        puts("98");
    }

    if (n > 98)
    {
        for(n; n > 98; n--)
            printf("%d, ", n);
        puts("98");
    }
}