#include <stdio.h>
#include <stdlib.h>

// String to Int
int stoi(char *str)
{
	int res;
	int flag;

	res = 0;
	flag = 1;
	if (*str == '-')
	{
		flag = -1;
		str++;
	}

	while (*str)
	{
		res = res * 10 + (*str - '0')*flag;
		str++;
	}

	return res;
}


// len.c function
int num_len(int num)
{
	int res;

	res = 0;
	while (num)
	{
		res++;
		num /= 10;
	}

	return res;
}


// Unsigned Int to String
char *itos(unsigned int num)
{
	char 			*res;
	unsigned int	len;
	unsigned int 	i;

	i = 0;
	len = num_len(num);
	res = (char*)malloc(len + 1);

	while (num)
	{
		res[len - 1 - i] = num % 10 + '0';
		num /= 10;
		i++;
	}
	
	res[len] = '\0';
	return res;
}