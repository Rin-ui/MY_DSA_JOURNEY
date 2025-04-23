#include<stdio.h>

void perfect_number(int n) { // ✅ Use void return type
    int divisor = 0;

    for(int i = 1; i < n; i++) {
        if(n % i == 0) { // ✅ Check if i is a divisor
            divisor += i;
        }
    }

    if(divisor == n) {
        printf("Perfect number: %d\n", n); // ✅ Use n, not i
    }
}

int main() {
    int n;

    printf("Enter a number till which we will find perfect numbers: ");
    scanf("%d", &n);

    for(int i = 1; i <= n; i++) {
        perfect_number(i); // ✅ Call function with i
    }

    return 0;
}
