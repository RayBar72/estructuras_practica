#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *non = list, *par = list;

	if (!list)
		return (0);
	while (par->next && par->next->next)
	{
		non = non->next;
		par = par->next->next;
		if (non == par)
		{
			return (1);
		}
	}
	return (0);
}
