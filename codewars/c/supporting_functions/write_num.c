#include <unistd.h>

void write_num(int a)
{
	char temp;

	if (a != 0)
	{
		write_num(a/10);
		temp = a%10 + '0';
		write(1, &temp, 1);
	}
}