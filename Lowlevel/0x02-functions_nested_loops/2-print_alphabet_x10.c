#include "main.h"


void print_alphabet_x10(void)
{
	int i = 0, j = 0;

	for (i = 0; i < 10; i++)
	{
		for (j = 'a'; j <= 'z'; j++)
			putchar(j);
		putchar('\n');
	}
}