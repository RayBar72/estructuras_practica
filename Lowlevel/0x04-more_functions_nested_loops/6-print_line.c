#include "main.h"

void print_line(int n)
{
    if (n > 0)
        while (n)
        {
            putchar('_');
            n--;
        }
    putchar('\n');
        
}