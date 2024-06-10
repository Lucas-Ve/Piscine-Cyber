#include <stdio.h>
#include <string.h>

int	main(void)
{
	char	str[100];

	printf("Please enter key: ");
	scanf("%99s", str);
	if (strcmp(str, "__stack_check"))
		printf("Nope.\n");
	else
		printf("Good job.\n");
	return (0);
}
