#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i = 0;

	for (i = 'a'; i <= 'z'; i++)
		putchar(i);
	for (i = 'A'; i <= 'Z'; i++)
		putchar(i);
	putchar('\n');
	return (0);
}