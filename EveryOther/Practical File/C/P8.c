#include <stdio.h>

void rev() {
    char ch;
    scanf("%c",&ch);
    
    if (ch == '\n') {
        printf("\n");
        return;
    }
    
    rev();
    printf("%c",ch);
}

int main() {

    printf("\n\tEnter a Sentence:\n");
    rev();

    return 0;
}