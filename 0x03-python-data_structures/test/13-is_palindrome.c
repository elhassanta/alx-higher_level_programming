#include "lists.h"
/**
 *rev_list - this function reverse a linked list
 *@head: parmeter pointer point to the head
 *@fnode: parameter to first node
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
	listint_t *temp = (*head), *comp1, *comp2;
	listint_t **head2 = NULL;
	int len = 0, count = 0;

	if ((!(*head)) || !head || (*head)->next == NULL)
		return (1);
	while (temp->next)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	while (count <= len / 2)
	{
		temp = temp->next;
		count++;
	}
	head2 = &temp;
	rev_list(head2, temp);
	comp1 = *head;
	comp2 = *head2;
	count = 0;
	while (count < len / 2)
	{
		if (comp1->n != comp2->n)
		{
			rev_list(head2, *head2);
			return (0);
		}
		comp1 = comp1->next;
		comp2 = comp2->next;
		count++;
	}
	rev_list(head2, *head2);
	return (1);
}
