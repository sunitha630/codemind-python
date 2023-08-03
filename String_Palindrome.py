def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s=input()
if(is_palindrome(s)):
    print('Palindrome')
else:
    print('Not Palindrome')

