#include <stdio.h>
#include <string.h>
#include <ctype.h>

int Find(int const *string, char c,int size) {

    int i;

    for ( i = 0; i < size; i += 2)
        if (string[i] == c) 
            return i;
    
    return -1;
}
int  len(char const* string) {
    int size = 0;

    for (;*string != '\0'; ++size,++string);

    return size;
}
void frequency(char* string) {

    int occur[2 *len(string)+1];

    int i , varSize = 0;

    for (i = 0; string[i] != '\0' ; i++) {

        int find = Find(occur , string[i] , varSize);

        if (find == -1) {
            occur[varSize] = string[i];
            occur[varSize+1] = 1;
            varSize += 2;
        }
        else 
            occur[find + 1] += 1;
    }

    for (i = 0; i < varSize; i+=2)
        printf("\n\t '%c' occurence is %d",(char)occur[i],occur[i+1]);

}

void Chnge(char *string) {

    int i , j;

    for(i = 0; string[i] != '\0'; i++) 
        if (!isalpha(string[i])) 
            for(j = i-- ;string[j] != '\0';j++) 
                string[j] = string[j+1];
    
    printf("\n\n\tYour string with alphabets only is:\t%s\n\n",string);
    
}
int main() {

    char string[] = "Hello, How are you";

    frequency(string);

    Chnge(string);

    return 0;
}