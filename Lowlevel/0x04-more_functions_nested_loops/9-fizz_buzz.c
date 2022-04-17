#include "main.h"

int main(void)
{
    int n = 1;

    for (; n <= 100; n++)
    {
        if (n % 15 == 0)
            printf("FizzBuzz ");
        else
        {
            if (n % 3 != 0 && n % 5 != 0)
                printf("%d ", n);
            else
            {
                if (n % 3 == 0)
                    printf("Fizz ");
                if (n % 5 == 0)
                    printf("Buzz ");
            }
        }
    }        
    puts("");
    return (0);
}