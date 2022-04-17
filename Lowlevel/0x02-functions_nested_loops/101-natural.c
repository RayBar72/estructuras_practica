#include "main.h"

int main(void)
{
    int num = 0, i = 0;

    for(i = 0; i < 1024; i++)
    {
        if (i % 3 == 0 && i % 15 != 0)
            num += i;
        else if (i % 5 == 0)
            num += i;
        printf("A %d la suma es = %d\n", i, num);
    }
    return (0);
}