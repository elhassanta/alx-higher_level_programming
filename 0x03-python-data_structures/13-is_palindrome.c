#include "lists.h"
/**
 *is_palindrome - check if a linked list is palindrome
 *@head: parameter pointer point to the head
 *Return: return 0 if palindrom or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = (*head);
	int *list = NULL;
	int len = 0, count = 0;

	if ((!(*head)) || !head)
		return (1);
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	list = malloc(len * sizeof(int));
	if (list == NULL)
		return (0);
	temp = *head;
	while (temp)
	{
		list[count] = temp->n;
		temp = temp->next;
		count++;
	}

	count = 0;
	len--;
	while (count <= len / 2)
	{
		if (list[count] != list[len - count])
		{
			free(list);
			return (0);
		}
		count++;
	}
	free(list);
	return (1);
}
