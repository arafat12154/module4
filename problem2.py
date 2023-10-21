print("Enter a length in inches (or a negative value to exit):")
while True:
    inches = float(input())
    if inches < 0:
        print("Exiting the program.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters")
