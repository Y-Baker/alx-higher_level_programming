#include "lists.h"

/**
 * is_palindrome - check if it palindrome or not
 * @head: the pointer to the list
 * Return: 1 if palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	if (!*head || !(**head).next)
		return (1);
	listint_t *first;
	int n, re;

	first = *head, n = first->n;
	while (first->next->next)
	{
		first = first->next;
	}
	if ((first->next)->n != n)
		return (0);
	free_listint(first->next);
	first->next = NULL;
	first = (*head)->next;
	re = is_palindrome(&first);
	if (re == 0)
		return (0);
	add_nodeint_end(head, n);
	return (1);
}


/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}
