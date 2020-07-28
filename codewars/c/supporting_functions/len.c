#include <stdio.h>

int str_len(char *str)
{
	int i;

	i = 0;
	while (*str++)
		i += 1;
	return i;
}

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

int main(int argc, char const *argv[])
{
	printf("%d\n", num_len(12034));
	return 0;
}