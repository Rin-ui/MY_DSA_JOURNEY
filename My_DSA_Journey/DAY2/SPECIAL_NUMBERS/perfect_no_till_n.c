#include<stdio.h>

int main(){
    int n;
    int sum = 0;

    printf("Enter a number till which we will find perfect numbers: ");
    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        int divisor = 0; // ✅ Reset for each number

        for(int j = 1; j <= i / 2; j++){ // ✅ j starts at 1 and goes up to i/2
            if(i % j == 0){
                divisor += j;
            }
        }

        if(divisor == i){
            printf("%d is a perfect number\n", i);
        }
    }

    return 0;
}
