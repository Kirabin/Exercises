#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>

void write_str(char *s)
{
	while (*s)
		write(1, s++, 1);
}

int str_len(const char *str)
{
	int i;

	i = 0;
	while (*str++)
		i += 1;
	return i;
}

char *camel_case(const char *s)
{
	char	*new_str;
	int		is_new_word;
	int		i;

	is_new_word = 1;
	new_str = (char*)malloc(str_len(s) + 1);
	i = 0;
	while (*s)
	{
		if ((*s <= 'z' && *s >= 'a') || 
			(*s <= 'Z' && *s >= 'A'))
		{
			if (is_new_word)
			{
				is_new_word = 0;
				new_str[i++] = *s - 'a' + 'A';
			}
			else
			{
				new_str[i++] = *s;
			}
		}
		else
		{
			is_new_word = 1;
		}
		s++;
	}
	new_str[i] = '\0';

	return new_str;
}

int main(int argc, char const *argv[])
{
	const char 	*s = "camel case method";
	char 		*res;
	res = camel_case(s);
	free(res);
	write_str(res);
	return 0;
}