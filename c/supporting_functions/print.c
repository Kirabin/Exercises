#include <unistd.h>
#include <stdio.h>

void ft_putnbr(int nbr)
{
	char temp;

	if (nbr != 0)
	{
		ft_putnbr(nbr/10);
		temp = nbr%10 + '0';
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