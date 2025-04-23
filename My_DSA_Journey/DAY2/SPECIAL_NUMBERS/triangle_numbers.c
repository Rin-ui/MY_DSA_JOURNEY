// triangular number == sum of natural numbers
#include <stdio.h>
#include <stdlib.h> // ✅ Added for exit()

int main(){
    int n;
    int sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);

    for(int i = 1; sum <= n; i++){
        sum = sum + i;
        if(sum == n){
            printf("YES\n");
            exit(0);
        }
    }
    printf("NO\n");
    return 0;
}



    
    