#include <stdio.h>


int main() {

    float marks[3][30];

    int max_stud[3];

    int i,j;

    printf("\n\tInput data:\n");

    for(i = 0; i < 3;i++) {

        printf("\n\tEnter number of students in class %d :",i+1);
        scanf("%d", &max_stud[i]);

        for (j = 0 ; j < max_stud; j++) {
            printf("\n\tEnter marks of class %d -> Student %d:",i+1,j+1);
            scanf("%f", &marks[i][j]);
        }
    }

    printf("\n\tAll marks entered are:\n");

    for (i = 0; i < 3; i++)
        for (j = 0; j < max_stud[i]; j++) 
            printf("\n\t Marks of student %d of class %d is: %f",j+1,i+1,marks[i][j]);

    return 0;
}