// https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/c

#include <unistd.h>

char findMissingLetter(char array[], int arrayLength)
{
	int i;

	i = 0;
	while (i < arrayLength - 1)
	{
		if (array[i] != array[i + 1] - 1)
			return array[i] + 1;
		i++;
	}
	return (' ');
}

int main(int argc, char const *argv[])
{
	char arr = { 'a','b','c','d','f' };
	int res;
	
	res = findMissingLetter(arr, 5);
	write(1, &res ,1); // 
}