#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i = 0;

	for (i = 'a'; i <= 'z'; i++)
		if (i != 'e' && i != 'q')
			putchar(i);
	putchar('\n');
	return (0);
}