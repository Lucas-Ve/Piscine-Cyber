#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void no() {
    printf("Nope.\n");
    exit(1);
}

void ok() {
    printf("Good jobs.\n");
    exit(0);
}

int main(void) {
    char local_39[25];
    char local_21[9];
    uint local_18;
    int local_14;
    int local_10;

    printf("Please enter key: ");
    local_10 = scanf("%24s", local_39);  // Limiter la taille de l'entrée pour éviter les débordements
    if (local_10 != 1) {
        no();
    }
    if (local_39[1] != '0') {
        no();
    }
    if (local_39[0] != '0') {
        no();
    }

    memset(local_21, 0, 9);
    local_21[0] = 'd';  // Initialisation avec 'd'
    local_18 = 2;
    local_14 = 1;

    while (true) {
        size_t sVar2 = strlen(local_21);
        bool bVar4 = false;
        if (sVar2 < 8) {
            sVar2 = strlen(local_39);
            bVar4 = local_18 < sVar2;
        }
        if (!bVar4) break;

        char temp[4] = {local_39[local_18], local_39[local_18 + 1], local_39[local_18 + 2], '\0'};
        int iVar3 = atoi(temp);
        local_21[local_14] = (char)iVar3;
        local_18 += 3;
        local_14 += 1;
    }
    local_21[local_14] = '\0';

    if (strcmp(local_21, "delabere") == 0) {
        ok();
    } else {
        no();
    }
    return 0;
}
