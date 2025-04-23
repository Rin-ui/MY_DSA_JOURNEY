// input must be entered in one line seperated by commas
#include<stdio.h>
int main(){
    int a,b,c;
    int sum;
    printf("enter 3 numbers seperated by commas : ");
    if(scanf("%d,%d,%d", &a,&b,&c)==3){
        sum = a +b+c;
        printf("sum is %d", sum);
    }
    else{
        printf("invalid format, put i/p seperated by commas");
    }
    
    return 0;


}