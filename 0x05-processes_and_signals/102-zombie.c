#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes.
 * Return: does not return
*/
int main(void)
{
	int i = 0;
	int pid_t = 0;

	for (i = 0; i < 5; i++)
	{
		pid_t = fork();
		if (pid_t > 0)
			printf("Zombie process created, PID: %i\n", pid_t);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
