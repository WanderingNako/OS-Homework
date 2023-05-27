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
        int m,n;
		m = transfer(argv[1]);
		n = transfer(argv[2]);
		if(m > n)
		{
			printf("min(%d,%d) is %d\n",m,n,n);
		}
		else
		{
			printf("min(%d,%d) is %d\n",m,n,m);
		}
        return 0;
}

