#include "lists.h"
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *actual, *previus;

	actual = malloc(sizeof(listint_t));
	actual = *head;
	actual->n = number;
	actual->next = NULL;
	if (!actual)
		return (NULL);
	previus = *head;
	while(previus->next)
	{

	}
}