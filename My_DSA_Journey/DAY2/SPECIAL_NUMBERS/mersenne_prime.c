#include <stdio.h>
#include <math.h>  // Include this to use the pow() function

int main(){
    int n;
    int count;
    int val;
    printf("Enter a number: ");
    scanf("%d", &n);

    for (int i = 2; i <= n; i++) {
        count = 0;  // Reset count to 0 for each iteration
        for (int j = 2; j <= i / 2; j++) {
            if (i % j == 0) {
                count++;
                break;  // If divisible, it's not a prime, break early
            }
        }

        if (count == 0) {  // Prime number
            val = (int)pow(2, i) - 1;  // Calculate Mersenne number
            // Now check if val is prime
            count = 0;  // Reset count for prime check of val
            for (int j = 2; j <= val / 2; j++) {
                if (val % j == 0) {
                    count++;
                    break;  // If divisible, val is not prime
                }
            }

            if (count == 0) {  // Mersenne number is prime
                printf("%d\n", val);
            }
        }
    }

    return 0;
}
