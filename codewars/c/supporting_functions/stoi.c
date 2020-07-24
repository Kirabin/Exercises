int stoi(char *str)
{
	int res;
	int flag;

	res = 0;
	flag = 1;
	if (*str == '-')
	{
		flag = -1;
		str++;
	}

	while (*str)
	{
		res = res * 10 + (*str - '0')*flag;
		str++;
	}

	return res;
}
