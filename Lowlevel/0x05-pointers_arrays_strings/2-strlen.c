#include "main.h"

int _strlen(char *s)
{
    int i = 0;

    while (*s)
    {
        *s++;
        i++;
    }
    return (i);
}