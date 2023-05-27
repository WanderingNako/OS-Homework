#include <stdio.h>
#include <string.h>

int transfer(char *s)
{
	int i,temp,f=1,sum=0;
	for(i = strlen(s) - 1;i >= 0;i--)
	{
		temp = s[i] - '0';
		temp *= f;
		f *= 10;
		sum += temp;
	}
	return sum;
}

int main(int argc,char *argv[])
{
        int m,n,l;
		float ave;
		m = transfer(argv[1]);
		n = transfer(argv[2]);
		l = transfer(argv[3]);
		ave = (m + n + l) / 3.0;
		printf("average(%d,%d,%d) is %.2f\n",m,n,l,ave);
        return 0;
}
