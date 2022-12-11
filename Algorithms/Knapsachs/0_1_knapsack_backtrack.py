# Define the items, weight limit, and values
items = ['item1', 'item2', 'item3']
weights = [10, 20, 30]
values = [60, 100, 120]
limit = 50

# Define a function to solve the problem using backtracking
def backtrack(current_value, current_weight, current_items):
    global max_value, max_items

    # Check if the current weight limit has been exceeded
    if current_weight > limit:
        return

    # Update the maximum value and items if a better solution is found
    if current_value > max_value:
        max_value = current_value
        max_items = current_items

    # Recursively explore the remaining items
    for i in range(len(items)):
        if items[i] not in current_items:
            backtrack(current_value + values[i], current_weight + weights[i], current_items + [items[i]])

# Initialize the maximum value and items
max_value = 0
max_items = []

if __name__ == '__main__':
    profits = [20,25,30]
    weights = [40,25,15]
    capacity = 50

# Solve the problem using backtracking
