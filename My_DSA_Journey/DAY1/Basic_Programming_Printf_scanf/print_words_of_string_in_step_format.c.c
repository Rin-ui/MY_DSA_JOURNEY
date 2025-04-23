#include<stdio.h>
#include<string.h>

int main(){
    char str[100];
    printf("Enter string: ");
    scanf("%[^\n]s", str);  // no & needed
    int len = strlen(str);  // get actual length of string

    for(int i = 0; i < len; i++){
        for(int j = i; j < len - 1; j++){  // spaces for alignment
            printf(" ");
        }
        printf("%c\n", str[i]);  // print one character per line
    }

    return 0;
}
