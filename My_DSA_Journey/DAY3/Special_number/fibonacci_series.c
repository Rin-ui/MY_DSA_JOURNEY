#include<stdio.h>

int main() {
    int range;
    int first, second, next;

    first = 0;
    second = 1;

    printf("enter the range: ");
    scanf("%d", &range);

    // ✅ Print first two Fibonacci numbers
    printf("%d ", first);
    printf("%d ", second);

    next = first + second;

    // ✅ Generate and print Fibonacci numbers until the range
    while(next <= range) {
        printf("%d ", next);
        first = second;
        second = next;
        next = first + second;
    }

    return 0;
}
