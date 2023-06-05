#include "lists.h"

/**
 * check_cycle - check if it cycle or not
 * @list: the linked list
 * Return: 0 if not , 1 if it cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *check;

	check = list;
	while (list->next)
	{
		list = list->next;
		if (list == check)
			return (1);
	}
	return (0);
}
