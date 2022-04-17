#include "main.h"

int main(void)
{
    long long num0 = 0, num1 = 1, num2 = 0, i = 1;

    while (num1 < (4000000 - num1))
    {
        num2 = num1 + num0;
        num0 = num1;
        num1 = num2;
        printf("Fibo de %lld = %lld\n", i, num2);
        i++;
    }
    return (0);
}