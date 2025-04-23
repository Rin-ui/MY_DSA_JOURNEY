// perfect number --> sum of all divisors of a number (except itself) gives same number

#include<stdio.h>
int main(){
    int n;
    int divisors = 0;
    printf("enter no: ");
    scanf("%d",&n);
    for(int i = 1; i<n; i++){
        if(n%i==0){
            divisors += i;
        }
        
    }
    if(divisors == n){
        printf("YES");
    }
    else{
        printf("NO");
    }
    return 0;


}