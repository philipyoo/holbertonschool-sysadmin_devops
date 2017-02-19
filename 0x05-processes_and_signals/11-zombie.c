#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infite_while - infinite loop
 * Return: 0
 */
int infite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function that creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
			sleep(1);
		else
			exit(0);
		printf("Zombie process created, PID: %d\n", child_pid);
	}

	infite_while();

	return (0);
}
