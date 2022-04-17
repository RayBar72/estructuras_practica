#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	int i = 0, j = 0;

	for (i = '0'; i <= '8'; i++)
	{
		for (j = '1'; j <= '9'; j++)
		{
			
			if (j > i)
			{
				putchar(i);
				putchar(j);
				if (i != '8' || j != '9')
					putchar(',');
					putchar(' ');
			}
		}
	}
	putchar('\n');
	return (0);
}