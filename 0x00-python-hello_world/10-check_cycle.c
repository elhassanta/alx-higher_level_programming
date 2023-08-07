#include "lists.h"

/**
 * check_cycle - this function will check if a linked list is list
 *@head : param pointer the head
 *Return: this function return 1 or 0
 */

int check_cycle(listint_t *head)
{
	listint_t *nextNode;

	if (head == NULL)
		return (0);
	while (nextNode = head->next)
	{
		if (nextNode >= head)
			return (1);
		head = nextNode;
	}
	return (0);

}
