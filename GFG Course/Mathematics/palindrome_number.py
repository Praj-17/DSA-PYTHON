# note that do not make the mistake of converting it to a string it will take more space as well as time and then you will have to iterate again

def is_palindrome(n):
    origin = n
    reverse = 0
    while n>0:
        last_digit = n%10
        reverse =  reverse*10 +last_digit
        n = n//10
    return origin == reverse

print(is_palindrome(101341))
