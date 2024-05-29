
# converting an iteger to a list takes O(n) time complexity
# the Space complexisty is O(d) where d is digits
def count_digits(n):
    return len(str(n))


# the while loop will run d times that is number of digit times, and the count variable will take constant space Hence the below program is better
def count_digit_standar(n):
    count = 0
    while n>0: 
        n = n//10
        count +=1
    return count

print(count_digit_standar(4814814))
print(count_digits(4814814))


