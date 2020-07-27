#include <stdio.h>
#include <stdlib.h>

int str_len(char *str)
{
	int i;

	i = 0;
	while (*str++)
		i += 1;

	return (i);
}

char* upper(char *str)
{
	int i;
	char *res;

	i = 0;
	res = (char*)malloc(str_len(str)+1);

	while(str[i])
	{
		if ('a' <= str[i] && str[i] <= 'z')
			res[i] = str[i] - 'a' + 'A';
		else
			res[i] = str[i];
		i++;
	}
	res[i] = '\0';

	return (res);
}

char upper_ch(char ch)
{
	if ('a' <= ch && ch <= 'z')
		return ch - 'a' + 'A';

	return (ch);
}

char* lower(char *str)
{
	int i;
	char *res;

	i = 0;
	res = (char *)malloc(str_len(str) + 1);

	while(str[i])
	{
		if ('A' <= str[i] && str[i] <= 'Z')
			res[i] = str[i] - 'A' + 'a';
		else
			res[i] = str[i];
		i++;
	}
	res[i] = '\0';

	return (res);
}

char lower_ch(char ch)
{
	if ('A' <= ch && ch <= 'Z')
		return ch - 'A' + 'a';

	return (ch);
}

int is_lower(char *str)
{
	while (*str)
	{
		if ('A' <= *str && *str <=  'Z')
			return (0);
		str++;
	}
	return (1);
}

int is_upper(char *str)
{
	while (*str)
	{
		if ('a' <= *str && *str <=  'z')
			return (0);
		str++;
	}
	return (1);
}

int is_alpha(char ch)
{
	if ('a' <= ch && ch <= 'z')
		return (1);
	if ('A' <= ch && ch <= 'Z')
		return (2);
	return (0);
}

char* title(char *str)
{
	int		new_word;
	int		i;
	char	*res;

	i = 0;
	new_word = 1;
	res = (char *)malloc(str_len(str) + 1);

	while (str[i])
	{
		if (is_alpha(str[i]))
		{
			if (new_word)
			{
				res[i] = upper_ch(str[i]);
				new_word = 0;
			}
			else
				res[i] = lower_ch(str[i]);
		}
		else
		{
			res[i] = str[i];
			new_word = 1;
		}
		i++;
	}
	res[i] = '\0';

	return (res);
}

char* capitalize(char *str)
{
	int		i;
	char*	res;

	i = 0;
	res = (char*)malloc(str_len(str) + 1);

	if (str[i])
	{
		res[i] = upper_ch(str[i]);
		i++;
	}

	while (str[i])
	{
		res[i] = lower_ch(str[i]);
		i++;
	}

	return (res);
}

int main()
{
	char *s = "a AaA SS sdgasd kirlsl";
	char *title_s;
	char *capitalize_s;

	title_s = title(s);
	capitalize_s = capitalize(s);
	printf("%s -> titled: %s\n", s, title_s);
	printf("%s -> capitalized: %s\n", s, capitalize_s);

	free(title_s);
	free(capitalize_s);
}