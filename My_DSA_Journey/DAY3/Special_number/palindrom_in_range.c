#include<stdio.h>

int main() {
    int limit;
    int num;
    int rem;
    int rev;

    printf("enter limit: ");
    scanf("%d", &limit);

    // Loop from 0 to limit
    for(int i = 0; i <= limit; i++) {
        num = i;      // Save original number
        rev = 0;      // ✅ FIX: Reset rev for every new number

        int temp = i; // ✅ FIX: Use a temporary variable so original 'i' is not modified
                      // ❌ MISTAKE: In your code, you were changing 'i' inside the loop, which caused the loop to break early and skip values.

        // Reverse the number
        while(temp > 0) {
            rem = temp % 10;
            rev = rev * 10 + rem;
            temp = temp / 10;
        }

        // Check if the number is a palindrome
        if(rev == num) {
            printf("%d ", num); // ✅ FIX: Print 'num' instead of 'i' (which is changed inside loop in your code)
                                // ❌ MISTAKE: You printed 'i', but inside your loop 'i' was being modified, so it printed 0.
        }
    }

    return 0;
}
