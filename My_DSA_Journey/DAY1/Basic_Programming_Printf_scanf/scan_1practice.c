#include <stdio.h>
int main(){
    char str[100];
    printf("Enter a string: ");
    // my task is printing a sentance with spaces by usimg scanf not by any external function
    // by default scanf reaf till space --> so we are gonna modify it as scanf will read till new line is encountered
    scanf("%[^\n]s",str);
    // now the sting we took input, we'll iterate over it till the end of string
    int i = 0;
    while(str[i] !='\0'){
        if(str[i] ==' '){
            printf("\n");
        }
        else{
            printf("%c",str[i]);
        }
        i++;
    }
    return 0;
}
