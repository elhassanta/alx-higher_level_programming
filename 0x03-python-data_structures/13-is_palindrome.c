#include "lists.h"
/**
 *rev_list - this function reverse a linked list
 *@head: parmeter pointer point to the head
 *Return: return reversed linked list
 */
void rev_list(listint_t **head, listint_t *fnode)
{
	listint_t *node = NULL;
	if (fnode->next == NULL)
	{
		*head = fnode;
		return;
	}
	rev_list(head, fnode->next);
	node = fnode->next;
	node->next = fnode;
	fnode->next = NULL;
}
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

	if ((!(*head)) || !head || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	list = malloc((len / 2) * sizeof(int));
	if (list == NULL)
		return (0);
	temp = *head;
	while (count < len / 2)
	{
		list[count++] = temp->n;
		temp = temp->next;
	}
	count = 0;
	rev_list(head, *head);
	temp = *head;
	while (count < len / 2)
	{
		if (list[count] != temp->n)
		{
			free(list);
			return (0);
		}
		temp = temp->next;
		count++;
	}
	free(list);
	return (1);
}
