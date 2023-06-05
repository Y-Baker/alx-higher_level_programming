#include "lists.h"

/**
 * check_cycle - check if it cycle or not
 * @list: the linked list
 * Return: 0 if not , 1 if it cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *check, *fast;

	if (!list)
		return (0);
	check = list;
	fast = list;
	while (list->next && list && fast && fast->next)
	{
		list = list->next;
		fast = fast->next->next;
		if (list == check)
			return (1);
		if (list == fast)
			return (1);
	}
	return (0);
}
