// https://www.codewars.com/kata/541c8630095125aba6000c00
#include "../supporting_functions/write_num.c"

int digit_sum(int num)
{
	int sum;

	sum = 0;
	while (num)
	{
		sum += num % 10;
		num /= 10;
	}
	return (sum);
}

int digital_root(int n) {

	while (n / 10 != 0)
		n = digit_sum(n);
	return (n);
}

int main(int argc, char const *argv[])
{
	write_num(digital_root(132189));
	return 0;
}
