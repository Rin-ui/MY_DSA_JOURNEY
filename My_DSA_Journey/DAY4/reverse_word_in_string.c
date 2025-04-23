#include <stdio.h>
#include <string.h>

int main() {
    char s[100], word[100];
    int i, j = 0, len, length;
    printf("Enter a string: ");

    // Take input string including spaces until newline
    scanf(" %[^\n]", s);

    length = strlen(s);  // Get the length of input string

    for(i = 0; i < length; i++) {
        // If the character is not a space and not end of string
        if(s[i] != ' ' && s[i] != '\0') {
            word[j++] = s[i];  // Store character in word[] and move j to next position
        } else {
            word[j] = '\0';       // Null-terminate the word
            len = strlen(word);   // Get length of the word

            // Print the word in reverse
            while(len > 0) {
                printf("%c", word[--len]);
            }

            printf(" ");  // Space between reversed words
            j = 0;        // Reset j for next word
        }
    }

    // To handle last word if there's no space after it
    word[j] = '\0';
    len = strlen(word);
    while(len > 0) {
        printf("%c", word[--len]);
    }

    return 0;
}
