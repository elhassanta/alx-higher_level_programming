#include "lists.h"

/**
 *check_cycle - this function will check if a linked list is list
 *@list : param pointer the head
 *Return: this function return 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *previouse = list;

	while (list)
	{
		list = list->next;
		if (list >= previouse)
			return (1);
		previouse = list;
	}
	return (0);
}
