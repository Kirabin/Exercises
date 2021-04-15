int sum(int *values, int count)
{
	int i;
	int sum;

	i = 0;
	sum = 0;
	while (i < count)
		sum += values[i++];

	return (sum);
}
