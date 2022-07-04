#include <stdio.h>

int main() {

    char str[1000];
    int Gets(char*,int);

    printf("\n\tEnter line: \t");

    while(Gets(str,0)) 
        printf("\n\t%s \n\n\tEnter new line: \t" , str);

    return 0;
}

int Gets(char *str,int i) {

    scanf("%c",&str[i]);

    if (str[i] == '\n') {
        str[i] = '\0';
        return i;
    }
    return Gets(str,i+1);
}


