// WAP to store n elements in an array and print the elements using pointer
#include <stdio.h>
#include <stdlib.h>


int main() {
    int n;
    int *arr;
    int i;

    printf("Enter the number of integers in the array: ");
    scanf("%d", &n);
    arr = (int*) calloc(n, sizeof(int));
    printf("\n");
    for(i=0; i<n; i++) {
        printf("Enter integer number %d: ", i+1);
        scanf("%d", &arr[i]);
    }

    printf("\n\033[1;97mINDEX: VALUE\033[0m\n");
    for(i=0; i<n; i++) {
        printf("%d: %d\n", i, *(arr+i));
    }

    printf("\n");
}