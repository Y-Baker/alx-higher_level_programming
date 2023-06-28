#include "lists.h"

int is_palindrome(listint_t **head)
{
    if (!*head || !(**head).next)
        return (1);
    listint_t *first;
    listint_t *last;
    int n, num;

    first = *head, n = first->n;
    while (first->next->next)
    {
        first = first->next;
    }
    if ((first->next)->n != n)
        return (0);
    first->next = NULL;
    first = (*head)->next;
    is_palindrome(&first);
}
