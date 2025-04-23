#include <stdio.h>

int main() {
    char str[100];  // Use a character array to store a string
    printf("enter string: ");
    scanf("%[^\n]s",str);
    int i = 0;
    while(str[i] != '\0'){ // checking till end of string using loop
        if(str[i] ==' '){
            printf("\n");
        }
        else{
            printf("%c", str[i]);
        }
        i++;

    }

    printf("\nthe o/p is \n : %s",str);
    return 0;
}
