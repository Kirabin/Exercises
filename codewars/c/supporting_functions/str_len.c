int str_len(char *str)
{
	int i;

	i = 0;
	while (*str++)
		i += 1;
	return i;
}