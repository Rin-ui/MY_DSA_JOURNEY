#include<stdio.h>
int main(){
    int n;
    int num;
    int rem;
    int sum = 0;
    printf("enter a number: ");
    scanf("%d",&n);
    num = n;
    do{
        sum =0;
        while(n!=0){
            rem = n % 10;
            sum = sum + rem * rem;
            n = n/10;
        }
        if(sum >=10){
            n = sum;
        } 
    }while(n >= 10);
    if(sum ==1){
        printf("happy number");
    }
    else{
        printf("not happy number");
    }
    return 0;
}