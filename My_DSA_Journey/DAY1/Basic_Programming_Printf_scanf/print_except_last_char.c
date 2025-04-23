#include<stdio.h>
int main(){
    char str[100];
    printf("Enter String: ");
    scanf("%[^\n]s",str);
    int i = 0;
    while(str[i]!='\0'){
        if(str[i+1]== ' ' || str[i+1]=='\0'){
            i++;
            continue;
        }
        else{
            printf("%c",str[i]);
            i++;
        }
    }
    return 0;
}