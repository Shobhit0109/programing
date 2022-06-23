//8a question

#include <stdio.h>
#include <math.h>

typedef struct Circle {
    float a,b,r; //Repesent Centre coordinates and circle radius repetively
} circle; //making a structure of name circle

int Check_Circle(circle c1,circle c2) { //function to check

    float dis_cent,dis_rad;
    dis_rad = c1.r + c2.r;
    if (dis_rad < 0)
        dis_rad *= -1;
    dis_cent = pow((pow(c1.a-c2.a,2) + pow(c1.b-c2.b,2)),0.5);

//in this algorithm, we check sum of radii of both ad differene in their centres
    if (dis_cent == dis_rad) 
        return 0;   //circles touch at a point
    else if (dis_cent < dis_rad)
        return 1; //circles intersecting
    else 
        return -1; //circles not interesecting
}

int main(void) {

    circle c1,c2;//2 reuqired cirles

// First cirle input
    printf("\n\tEnter Coordinates of center and radius of first circle in (a,b,r) format:");
    scanf("%f %f %f",&c1.a,&c1.b,&c1.r);

//Second circle input
    printf("\n\tEnter Coordinates of center and radius of Second circle in (a,b,r) format:");
    scanf("%f %f %f",&c2.a,&c2.b,&c2.r);

//Process Function
    switch(Check_Circle(c1,c2)) { //chek in switch-case
        case 1:
            printf("\n\tCircles are Intersecting");
            break;
        case -1:
            printf("\n\tCircles are not lintersecting");
            break;
        case 0:
            printf("\n\tCircles are touching");
    }
    return 0;
}

//8b question

#include <stdio.h>
#include <stdlib.h>
#define in(i,j,n) i*n + j //index of 1d array when emulating a 2d array

//based on concept of emulating 2d array

void printMatrix(int *arr,int n) {
    int i,j;

    for(i=0;i<n;i++) {

        printf("\n\t");
        for (j=0;j<n;j++)
            printf("%d ",arr[in(i,j,n)]);
    }
}

int main(void) {

    int n,*arr;
    int i,j,temp;

    printf("\n\tEnter size of Square matrix:");
    scanf("%d",&n);

    arr = (int*)malloc(n*n*sizeof(int)); //emulating 2d array in 1d 

    //Input elements in array
    for(i=0;i<n;i++) 
        for(j=0;j<n;j++) {
            printf("\n\tEnter element in %d row and %d column :",i+1,j+1);
            scanf("%d",&arr[in(i,j,n)]);
        }

    //Printing of input Matrix
    printf("\n\tInput matrix is:");
    printMatrix(arr,n);

    //Process
    for(i=0;i<n;i++)  //for upr upper main diagonal triangle we intercange with lower main diagonal triangle 
        for(j=i;j<n;j++) {
            temp = arr[in(i,j,n)];
            arr[in(i,j,n)] = arr[in(j,i,n)];
            arr[in(j,i,n)] = temp;
        }

    //Printing of result matrix
    printf("\n\tInput matrix is:");
    printMatrix(arr,n);


    free(arr); //free up memory
    return 0;
}


//8C question

#include <stdio.h>
#include <stdlib.h>
#define in(i,j,n) i*n + j //index of 1d array when emulating a 2d array

//based on concept of emulating 2d array

int checkEle(int *arr,int n,int index) {
    int i;
    int num = arr[index];
    for(i=0;i<n*n;i++)
        if (index != i && (arr[i] == num || num > n*n || num < 1))
            return 0;

    return 1;
}

void printMatrix(int *arr,int n) {
    int i,j;

    for(i=0;i<n;i++) {

        printf("\n\t");
        for (j=0;j<n;j++)
            printf("%d ",arr[in(i,j,n)]);
    }
}

int checkMagic(int *arr,int n) {

    int i,j;

    //check Rows
    {
        int k = -1;
        int sum[2] = {0};

        for (j = 0; j < n;j++) 
            sum[0] += arr[in(0,j,n)];

        for (i = 1;i < n;i++) {
            if (k == -1) {
                sum[1] = 0;
                for (j=1;j < n;j++) {
                    sum[1] += arr[in(i,j,n)];
                }
                k *= -1;
            }
            else {
                sum[0] = 0;
                for (j=1;j < n;j++) {
                    sum[0] += arr[in(i,j,n)];
                }
                k *= -1;
            }
            if (sum[0] != sum[1])
                return 0;
        }
    }

    //check column
    {
        int k = -1;
        int sum[2] = {0};

        for (i = 0; i < n;j++) 
            sum[0] += arr[in(i,0,n)];

        for (j = 1;j < n;j++) {
            if (k == -1) {
                sum[1] = 0;
                for (i=1;i < n;i++) {
                    sum[1] += arr[in(i,j,n)];
                }
                k *= -1;
            }
            else {
                sum[0] = 0;
                for (i=1;i < n;i++) {
                    sum[0] += arr[in(i,j,n)];
                }
                k *= -1;
            }
            if (sum[0] != sum[1])
                return 0;
        }
    }

    //check diagonals
    {
        int sum[2] = {0};
        for(j = 0;j < n;j++) //main diagonal
            sum[0] += arr[in(j,j,n)];

        for (j = 0;j < n;j++)
            sum[1] += arr[in(n-j-1,j,n)];

        if (sum[0] != sum[1])
            return 0;
    }

    return 1;
}

int main(void) {

    int n,*arr;
    int i,j;

    //Input the size of matrix
    printf("\n\tEnter size of Matrix:");
    scanf("%d",&n);

    arr = (int*)malloc(n*n*sizeof(int)); //emulating 2d array in 1d 
    for(i=0;i<n*n;i++)
        arr[i] = -1;

    //Input elements in array
    printf("\n\tRules every element of matrix should be unique and in range of [1,n*n]");
    for(i=0;i<n;i++) 
        for(j=0;j<n;j++) {

            printf("\n\tEnter element in %d row and %d column :",i+1,j+1);
            scanf("%d",&arr[in(i,j,n)]);

            if(!checkEle(arr,n,in(i,j,n))) {
                    printf("\n\tYou entered wrong input please follow rules and enter gain the element");
                    j--;
            }
        }
    //Printing of input Matrix
    printf("\n\tInput matrix is:");
    printMatrix(arr,n);

    if(checkMagic(arr,n)) 
        printf("\n\tIt is a magic matrix");
    else
        printf("\n\tIt is not a magic matrix");

    free(arr); //free the memory
    return 0;
}