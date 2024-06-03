def sum_of_digits_iterative(n):
    sum = 0
    while n>0:
        last_digit = n%10
        n //=10
        sum +=last_digit
    return sum

def recursive(n):
        if  n <10:
            return n

        return recursive(n//10) + n%10

    

print(recursive(253))
