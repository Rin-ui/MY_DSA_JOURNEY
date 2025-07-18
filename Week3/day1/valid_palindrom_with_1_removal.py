class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                def is_palindrome(substring):
                    return substring == substring[::-1]
                return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
            else:
                left +=1
                right-=1
        return True
