#include<stdio.h>
int main(){
    int n;
    int num;
    int rem;
    int rev = 0;
    printf("enter a number: ");
    scanf("%d",&n);
    num = n;
    
    while(n>0){
       
        rem = n%10;
        rev = rev * 10 + rem;
        n = n/10;
        
    }
    if(rev == num){
        printf("Palindrome");
    }
    else{
        printf("not Palindrome");
    }
    return 0;
}
