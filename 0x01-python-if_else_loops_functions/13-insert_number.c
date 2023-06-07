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

	if (*head == NULL)
	{
		add_nodeint_end(head, number);
		return (*head);
	}
	new = *head, last = NULL;
	while (new->next)
	{
		if (new->n > number)
		{
			added = malloc(sizeof(listint_t));
			if (!added)
				return (NULL);
			added->n = number;
			if (!last)
			{
				added->next = new;
				*head = added;
				return (*head);
			}
			added->next = last->next;
			last->next = added;
			return (*head);
		}
		last = new;
		new = new->next;
	}
	add_nodeint_end(head, number);
	return (*head);
}
