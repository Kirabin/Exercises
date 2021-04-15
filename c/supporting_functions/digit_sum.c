/*
	get integer 123 and return sum of it's digits 6
*/

int digit_sum(int num)
{
	int sum;

	sum = 0;
	while (num)
	{
		sum += num % 10;
		num /= 10;
	}
	return (num);
}