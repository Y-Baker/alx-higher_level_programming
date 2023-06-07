#include "lists.h"

/**
 * insert_node - insert the node in their place
 * @head: the head of the node
 * @number: the value
 * Return: the new list after edit
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *last, *added;

	new = *head, last = *head;
	while (new->next)
	{
		if (new->n > number)
		{
			added = malloc(sizeof(listint_t));
			if (!added)
				return (NULL);
			added->n = number;
			added->next = last->next;
			last->next = added;
			break;
		}
		last = new;
		new = new->next;
	}
	return (*head);
}
