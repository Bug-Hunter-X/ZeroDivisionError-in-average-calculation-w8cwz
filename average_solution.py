def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to prevent ZeroDivisionError
    return sum(numbers) / len(numbers)

#Example Usage
list1 = [10,20,30,40,50]
list2 = []
print(f"Average of {list1}: {calculate_average(list1)}")
print(f"Average of {list2}: {calculate_average(list2)}"