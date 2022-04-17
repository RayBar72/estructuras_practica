#include <stdlib.h>
#include <stdio.h>
#include <time.h>
/* more headers goes there */

/* betty style doc for function main goes there */
int main(void)
{
	int n, last;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	last = n % 10;
	printf("Last digi of %d is %d ", n, last);
	if (last == 0)
		puts("and is zero");
	else if (last > 6)
		puts("and is greater than 5");
	else if (last < 6)
		puts("and is less than 6 and not 0");
	return (0);
}