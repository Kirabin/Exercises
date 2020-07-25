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
	int len;
	int i;
	char *res;

	i = 0;
	len = str_len(str);
	res = (char*)malloc(len+1);

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

char* lower(char *str)
{
	int len;
	int i;
	char *res;

	i = 0;
	len = str_len(str);
	res = (char*)malloc(len+1);

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

int is_lower(char *str)
{
	while (*str)
	{
		if ('A' <= *str && *str <=  'Z')
			return (0);
		if (!('a' <= *str && *str <= 'z'))
			return (0);
		str++;
	}
	return (1);
}

int main()
{
	char *s = "a12AaASS2";
	char *lower_s;
	char *upper_s;

	lower_s = lower(s);
	upper_s = upper(s);
	printf("%s\n", lower_s);
	printf("%s\n", upper_s);

	printf("%d, %d\n", is_lower(lower_s), is_lower("qfsdf"));

	free(lower_s);
	free(upper_s);
}