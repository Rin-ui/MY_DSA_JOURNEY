#include<stdio.h>
#include<math.h>

int perfect_square(int x){
    int i;
    i = sqrt(x);
    return(i*i == x);
}
int main(){
    int n, result;
    printf("Enter a number: ");
    scanf("%d",&n);
    result = perfect_square(5*n*n+4) || perfect_square(5*n*n-4); 
    if(result ==1){   // as or operator returns either 0 or 1.
        printf("fibonacci");
    }
    else{
        printf("not fibonacci");
    }return 0;
}