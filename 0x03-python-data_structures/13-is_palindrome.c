#include "lists.h"
/**
 *rev_list - this function reverse a linked list
 *@head: parmeter pointer point to the head
 *@fnode: parameter to first node
 *Return: return reversed linked list
 */
#include "lists.h"

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
	listint_t *temp = (*head), *comp1;
	listint_t *head2 = NULL;
	int len = 0, count = 1;

		if (((*head) == NULL) || head == NULL)
			return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	if (len == 1)
		return (1);
	temp = *head;
	while (count < len / 2)
	{
		temp = temp->next;
		count++;
	}
	if ((len % 2) == 0 && temp->n != temp->next->n)
		return (0);
	if (len == 2)
		return (1);
	else if (len == 3)
	{
		if ((*head)->n == (*head)->next->next->n)
			return (1);
		else
			return(0);
	}
	temp = temp->next->next;
	head2 = temp;
	rev_list(&head2, temp);
	comp1 = *head;
	temp = head2;
	count = 1;
	while (count < len / 2)
	{
		if (comp1->n != temp->n)
		{
			rev_list(&head2, head2);
			return (0);
		}
		comp1 = comp1->next;
		temp = temp->next;
		count++;
	}
	rev_list(&head2, head2);
	return (1);
}
