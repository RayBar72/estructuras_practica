#include "main.h"

int print_last_digit(int c)
{
    int x = c;

    if (x < 0)
        x = -x;
    x = x % 10;
    putchar(x + '0');
    return (x);
}