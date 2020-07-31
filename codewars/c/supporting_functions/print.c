#include <unistd.h>

void ft_putnbr(int a)
{
	char temp;

	if (a != 0)
	{
		ft_putnbr(a/10);
		temp = a%10 + '0';
		write(1, &temp, 1);
	}
}

void ft_putstr(char *s)
{
	while (*s)
		write(1, s++, 1);
}

void ft_putchar(char c)
{
	write(1, &c, 1);
}