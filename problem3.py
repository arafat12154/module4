numbers = []
print("Enter numbers (empty string to quit):")
while True:
    user_input = input()
    if user_input == "":
        break
      try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.
if len(numbers) == 0:
    print("No numbers were entered.")
else:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
