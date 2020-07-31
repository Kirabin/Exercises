#include <stdio.h>
#include <stdlib.h>

typedef struct	s_list 
{
	int value; 
	struct s_list *next;
}		t_list;

void	push_left(t_list **list, int value)
{
	t_list *tlp = NULL;
	
	if (!(tlp = (t_list*)malloc(sizeof(t_list))))
		return ;

	tlp->value = value;
	tlp->next  = *list;
	*list      = tlp;
}

void	push_right(t_list **list, int value)
{
	t_list *tlp = *list;
	t_list *prev = NULL;

	while (tlp != NULL)
	{	
		prev = tlp;
		tlp = tlp->next;
	}
	
	tlp = (t_list*)malloc(sizeof(t_list));

	tlp->next = NULL;
	tlp->value = value;

	if (*list == NULL)
		*list = tlp;
	else
		prev->next = tlp;
}

int		pop_right(t_list *list)
{
	int	retval = 0;
	t_list	*node = list;

	// if where's only one value
	if (node->next == NULL)
	{
		retval = node->value;
		free(node);
		list = NULL;                   //should i assign null ?
		return (retval);	
	}
		
	while (node->next->next != NULL)
		node = node->next;
	
	retval = node->next->value;
	free(node->next);
	node->next = NULL;
	return (retval);
}

int		pop_left(t_list **list)
{
	int retval = 0;
	
	t_list *node = *list;
	retval = node->value;
	*list = (*list)->next;
	free(node);
	return (retval);
}

void	print_list(t_list *list)
{
	while (list)
	{
		printf("%d ", list->value);
		list = list->next;
	}
	printf("\n");
}

void	swap(t_list *list, int first_i, int second_i)
{
	int i;
	int swap_var;
	t_list *first = list, *second = list;

	i = 0;
	while (i < first_i)
	{
		if (first->next == NULL)
			return ;
		first = first->next;
		i++;
	}

	i = 0;
	while (i < second_i)
	{
		if (second->next == NULL)
			return ;
		second = second->next;
		i++;
	}
	swap_var = first->value;
	first->value = second->value;
	second->value = swap_var;
}

void	merge(t_list *first_l, t_list *second_l)
{
	while (first_l->next != NULL && first_l != NULL)
		first_l = first_l->next;

	while (second_l != NULL)
	{
		first_l->next = (t_list*)malloc(sizeof(t_list));
		first_l = first_l->next;
		first_l->value = second_l->value;
		second_l = second_l->next;
	}
}

void	clear(t_list **list)
{
	t_list *next = NULL;

	while (*list != NULL)
	{
		next = *list;
		*list = next->next;
		free(next);
	}
	*list = NULL;
}