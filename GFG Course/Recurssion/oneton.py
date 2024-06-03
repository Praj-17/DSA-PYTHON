def print_numbers(n):
    if n ==0:
        return
    print_numbers(n-1)
    print(n)
def print_numbers_reversed(n):
    if n ==0:
        return
    print(n)
    print_numbers_reversed(n-1)

print_numbers_reversed(5)