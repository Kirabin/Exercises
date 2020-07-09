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

int solution(int number) {
	int sum;
	int i;

	sum = 0;
	i = -1;
	while (++i < number)
	{
		if (i % 3 == 0 || i % 5 == 0)
			sum += i;
	}

	return (sum);
}

int main(){

	write_num(solution(10));
}