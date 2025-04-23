#include<stdio.h>
int main(){
    int n;int res;
    printf("Enter a number: ");
    scanf("%d",&n);
    res = (n%2 ==0) ? printf("Even") : printf("Odd");
    return 0;
}