#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

int main()
{
	pid_t n = fork();
	assert(-1 != n);

	if(n == 0) //Child1
	{
		printf("Child1:%d\n",getpid());
	}
	else //Father
	{
		pid_t pid = fork();
		assert(pid != -1);
		if(pid == 0) //Child2
		{
			printf("Child2:%d\n",getpid());
		}
		else
		{
			sleep(1);
			printf("Father:%d, Child1:%d, Child2:%d\n",getpid(),n,pid);
		}
	}
	
	exit(0);
}
