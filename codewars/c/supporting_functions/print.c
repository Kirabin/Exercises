#include <unistd.h>

void print_num(int a)
{
	char temp;

	if (a != 0)
	{
		print_num(a/10);
		temp = a%10 + '0';
		write(1, &temp, 1);
	}
}

void print_str(char *s)
{
	while (*s)
		write(1, s++, 1);
}