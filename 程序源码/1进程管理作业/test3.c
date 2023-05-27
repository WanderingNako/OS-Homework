#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>

int main()
{
        pid_t pid;
        int data=10;
		char cmd[100];
		char max[]={"max"};
		char min[]={"min"};
		char average[]={"average"};
		char quit[]={"quit"};
		char dest1[4]={0};
		char dest2[5]={0};
		char dest3[8]={0};
		char m[10]={0},n[10]={0},l[10]={0};
		char ch;
		int i,j;
		
        while(1){
                printf("Please Input A Command:");
                gets(cmd);
				strncpy(dest1,cmd,3);
				strncpy(dest2,cmd,4);
				strncpy(dest3,cmd,7);
                if(!strcmp(dest1,max)) //max(m,n)
				{
                    pid=fork();
                    if(pid>0)
					{
                        wait(NULL);
                    }
                    if(pid==0)
					{
						i=4;
						j=0;
						while((ch=cmd[i]) != ' ')
						{
							m[j]=ch;
							j++;
							i++;
						}
						m[j]='\0';
						i++;
						j=0;
						while((ch=cmd[i]) != '\0')
						{
							n[j]=ch;
							j++;
							i++;
						}
						n[j]='\0';
                        if(execl("./max","max",m,n,NULL) == -1)
						{
							printf("max execl failed!\n");
							perror("Why");
						}
						exit(0);
                    }
                }
				else if(!strcmp(dest1,min)) //min(m,n)
				{
					pid=fork();
                    if(pid>0)
					{
                        wait(NULL);
                    }
                    if(pid==0)
					{
                        i=4;
						j=0;
						while((ch=cmd[i]) != ' ')
						{
							m[j]=ch;
							j++;
							i++;
						}
						m[j]='\0';
						i++;
						j=0;
						while((ch=cmd[i]) != '\0')
						{
							n[j]=ch;
							j++;
							i++;
						}
						n[j]='\0';
                        if(execl("./min","min",m,n,NULL) == -1)
						{
							printf("min execl failed!\n");
							perror("Why");
						}
						exit(0);
                    }
				}
				else if(!strcmp(dest3,average)) //average(m,n,l)
				{
					pid=fork();
                    if(pid>0)
					{
                        wait(NULL);
                    }
                    if(pid==0)
					{
                        i=8;
						j=0;
						while((ch=cmd[i]) != ' ')
						{
							m[j]=ch;
							j++;
							i++;
						}
						m[j]='\0';
						i++;
						j=0;
						while((ch=cmd[i]) != ' ')
						{
							n[j]=ch;
							j++;
							i++;
						}
						n[j]='\0';
						i++;
						j=0;
						while((ch=cmd[i]) != '\0')
						{
							l[j]=ch;
							j++;
							i++;
						}
						l[j]='\0';
                        if(execl("./average","average",m,n,l,NULL) == -1)
						{
							printf("average execl failed!\n");
							perror("Why");
						}
						exit(0);
                    }
				}
				else if(!strcmp(dest2,quit)) //quit
				{
					break;
				}
				else{
                    printf("Command Not Found!\n");
                }
        }
		exit(0);
        return 0;
}
