#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void __syscall_malloc() {
    printf("Nope.\n");
    exit(1);
}

void ___syscall_malloc() {
    printf("Good Job.\n");
    exit(0);
}

int main(void) {
    ulong uVar1;
    int iVar2;
    size_t sVar3;
    bool bVar4;
    char local_4c;
    char local_4b;
    char local_4a;
    char local_48[31];
    char local_29[9];
    ulong local_20;
    int local_18;
    int local_14;
    int local_10;
    int local_c;

    local_c = 0;
    printf("Please enter key: ");
    local_10 = scanf("%30s", local_48);
    if (local_10 != 1)
        __syscall_malloc();
    if (local_48[1] != '2')
        __syscall_malloc();
    if (local_48[0] != '4')
        __syscall_malloc();
    fflush(stdin);
    memset(local_29, 0, 9);
    local_29[0] = '*';                                      
    local_20 = 2;
    local_14 = 1;

    while (true) {
        sVar3 = strlen(local_29);
        uVar1 = local_20;
        bVar4 = false;
        if (sVar3 < 8) {
            sVar3 = strlen(local_48);
            bVar4 = uVar1 < sVar3;
        }
        if (!bVar4) break;
        local_4c = local_48[local_20];
        local_4b = local_48[local_20 + 1];
        local_4a = local_48[local_20 + 2];

        char temp[4] = {local_4c, local_4b, local_4a, '\0'};
        iVar2 = atoi(temp);

        local_29[local_14] = (char)iVar2;
        local_20 += 3;
        local_14 += 1;
    }
    local_29[local_14] = '\0';
    local_18 = strcmp(local_29, "********");

    if (local_18 == -2)
        __syscall_malloc();
    else if (local_18 == -1)
        __syscall_malloc();
    else if (local_18 == 0)
        ___syscall_malloc(); // Si local_29 est "********", on appelle ___syscall_malloc
    else if (local_18 == 1)
        __syscall_malloc();
    else if (local_18 == 2)
        __syscall_malloc();
    else if (local_18 == 3)
        __syscall_malloc();
    else if (local_18 == 4)
        __syscall_malloc();
    else if (local_18 == 5)
        __syscall_malloc();
    else if (local_18 == 0x73)
        __syscall_malloc();
    else
        __syscall_malloc();
    return 0;
}