#include<stdio.h>
#include<stdlib.h>

int main(){
    int a;
    int first, second, next;

    first = 0;
    second = 1;

    printf("enter number: ");
    scanf("%d", &a);

    // Special case handling
    if(a == 0 || a == 1){
        printf("fibonacci number");
        return 0;
    }

    next = first + second;  // ✅ FIX: Initialize 'next' before using it in while condition

    while(next <= a){
        if(next == a){
            printf("fibonacci number");
            exit(0);
        }
        first = second;
        second = next;
        next = first + second;
    }

    // If not found in Fibonacci series
    printf("not fibonacci number");

    return 0;
}
