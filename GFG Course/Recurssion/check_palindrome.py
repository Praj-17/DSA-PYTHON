# String
def check_palindrome(s):
    if len(s) ==0 or len(s) ==1:
        return True
    return (s[0]==s[-1]) & check_palindrome(s[1:len(s)-1])

print(check_palindrome("abba1"))

# Number

"""
1   1   2   2   3   3 
"""
print(112233%10000)
