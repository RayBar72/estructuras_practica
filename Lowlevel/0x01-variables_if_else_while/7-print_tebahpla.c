#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i = 0;

	for (i = 'z'; i >= 'a'; i--)
		putchar(i);
	putchar('\n');
	return (0);
}