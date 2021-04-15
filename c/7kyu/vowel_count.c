#include <stddef.h>
#include "../supporting_functions/write_num.c"

size_t	get_count(const char *s)
{
	char	temp;
	const char	*i;
	int		count;

	count = 0;
	i = s;
	while (*i != '\0')
	{
		temp = *i++;
		if (temp == 'a' ||
			temp == 'e' ||
			temp == 'i' ||
			temp == 'o' ||
			temp == 'u')
			count++;
	}

	return (count);
}

int		main()
{
	char *s;

	s = "abracadabra";
	write_num(get_count(s));
}