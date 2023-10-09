#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: the head address of the linked list
 *
 * Return: 1 if it's a palindrome, 0 else
 */
int is_palindrome(listint_t **head)
{
    int i = 0, j = 0, num[sizeof(listint_t)];
    listint_t *cur = *head;

	if (*head)
	{
		while (cur)
		{
			num[i] = cur->n;
			cur = cur->next;
			i++;
		}

		while (j < i / 2)
		{
			if (num[j] == num[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}