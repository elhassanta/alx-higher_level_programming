#include "lists.h"
/**
 *insert_node - function in C that inserts a number into linked list
 *@number: parameter integer
 *@head: pointer point to the head
 *Return: pointer ot the head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *next;
	listint_t *curr = (*head);

	if (head == NULL)
		return (NULL);
	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);
	tmp->n = number;
	tmp->next = NULL;
	if (curr == NULL || curr->n >= number)
	{
		tmp->next = curr;
		*head = tmp;
		return (tmp);
	}
	while ((next = curr->next) != NULL)
	{
		if (curr->n >= number)
		{
			tmp->next = curr->next;
			curr->next = tmp;
			return (tmp);
		}
		curr = next;
	}
	curr->next = tmp;
	return (tmp);


}
