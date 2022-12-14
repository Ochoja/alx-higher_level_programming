#include "lists.h"

/**
 * insert_node - inserts node in a sorted linked list
 * @head: pointer to pointer head node
 * @number: number to be inserted
 * Return: pointer to new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *hold = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	new_node->n = number;
	new_node->next = NULL;

	if (new_node)
	{
		if (number <= (*head)->n)
		{
			new_node->next = (*head)->next;
			(*head)->next = new_node;
			return (new_node);
		}
		else
		{
			while (number > hold->n)
			{
				hold = hold->next;
			}
			new_node->next = (hold->next)->next;
			hold->next = new_node;
			return (new_node);
		}
	}

	return (NULL);
}
