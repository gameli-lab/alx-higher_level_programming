#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *second_half, *temp;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1; /* Empty list or a list with one element is a palindrome */

    slow = fast = *head;
    prev_slow = NULL;

    /* Use fast and slow pointers to find the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        temp = slow;
        slow = slow->next;
        temp->next = prev_slow;
        prev_slow = temp;
    }

    /* Check if the length of the list is odd and adjust pointers */
    if (fast != NULL)
        slow = slow->next;

    /* Now slow points to the start of the second half, and prev_slow to the end of the first half */

    second_half = slow;

    /* Compare the first half and the reversed second half */
    while (prev_slow != NULL && second_half != NULL)
    {
        if (prev_slow->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }

        prev_slow = prev_slow->next;
        second_half = second_half->next;
    }

    /* Restore the original state of the list (if required) */
    prev_slow = NULL;
    while (slow != NULL)
    {
        temp = slow->next;
        slow->next = prev_slow;
        prev_slow = slow;
        slow = temp;
    }
    *head = prev_slow;

    return is_palindrome;
}

